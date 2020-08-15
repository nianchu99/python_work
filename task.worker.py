import time, sys, queue
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

sever_addr = '127.0.0.1'
print("Connect to sever %s..." % sever_addr)

m = QueueManager(address=(sever_addr, 5000), authkey=b'bowenkei')
m.connect()

task = m.get_task_queue()
result = m.get_resule_queue()
for i in  range(10):
    try:
        n = task.get(timeout=1)
        print("run task %d % %d..." % (n ,n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)

    except queue.Queue.Empty:
        print("task queue is empty.")

print('worker exit.')

