from __future__ import annotations

import contextlib
import json
import pathlib
import random
import shutil
import subprocess
import time
from typing import Generator, Iterable, NoReturn

import huey as _huey
import np_logging
import np_session
import np_tools
from typing_extensions import Literal

from np_queuey.queues.pipeline_npexp_upload_queue import PipelineNpexpUploadQueue
from np_queuey.queues.pipeline_sorting_queue import PipelineSortingQueue
from np_queuey.types import Job, JobT, SessionArgs
from np_queuey.utils import get_job, get_session, update_status

logger = np_logging.getLogger()

huey = _huey.SqliteHuey('npexp_upload.db', immediate=True)

Q = PipelineNpexpUploadQueue()

@huey.task()
def upload_outstanding_sessions() -> None:
    job: Job | None = Q.next()
    if job is None:
        logger.info('No outstanding sessions in npexp_upload queue')
        return
    if Q.is_started(job):
        logger.info('Upload already started for %s', job.session)
        return
    run_upload(job)

def run_upload(session_or_job: Job | SessionArgs) -> None:
    job = get_job(session_or_job, Job)
    np_logging.web('np_queuey').info('Starting raw data upload to npexp %s', job.session)
    with update_status(Q, job):
        start_upload(job)
        add_to_pipeline_sorting_queue(job)
    np_logging.web('np_queuey').info('Validated raw data on npexp %s', job.session)

def start_upload(session_or_job: Job | SessionArgs) -> None:
    session = get_session(session_or_job)
    for src in raw_data_folders(session):
        dest = session.npexp_path / src.name
        logger.info(f'Copying {src} to {dest}')
        subprocess.run([
            'robocopy', f'{src}', f'{dest}',
            '/E', '/COPYALL', '/J', '/R:3', '/W:1800', '/MT:32'
            ], check=False) # return code from robocopy doesn't signal failure      
    # checksum validate copies after copying (since exception raised on
    # invalid copies)
    for src in raw_data_folders(session):
        dest = session.npexp_path / src.name
        np_tools.copy(src, dest)
        logger.info(f'Checksum-validated copy of {src} at {dest}')

def raw_data_folders(session_or_job: Job | SessionArgs) -> Iterable[pathlib.Path]:
    session = get_session(session_or_job)
    for drive in ('A:', 'B:'):
        for src in pathlib.Path(drive).glob(f'{session}*'):
            yield src
    
def add_to_pipeline_sorting_queue(session_or_job: Job | SessionArgs) -> None:
    PipelineSortingQueue().add_or_update(session_or_job)

                
def main() -> NoReturn:
    """Run synchronous task loop."""
    while True:
        upload_outstanding_sessions()
        time.sleep(300)
                
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)
    main()
