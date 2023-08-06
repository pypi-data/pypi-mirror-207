from np_queuey.queues.sqlite_isilon_queue import SqliteJobQueue
   
class PipelineQCQueue(SqliteJobQueue):
    
    table_name = 'qc'