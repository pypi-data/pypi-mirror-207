from np_queuey.queues.sqlite_isilon_queue import SqliteJobQueue
   
class PipelineNpexpUploadQueue(SqliteJobQueue):
    
    table_name = 'npexp_upload'