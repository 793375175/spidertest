import gevent
from gevent import monkey
from gevent.pool import Pool
import time
from queue import Queue

monkey.patch_all()
q = Queue()

def put_data():
    for i in range(10):
        print("添加")
        q.put(i)
        time.sleep(0.1)

def get_data():
    # for i in range(q.qsize()):
    while True:
        print(q.get())
        time.sleep(0.2)
        q.task_done()

p = Pool()

p.apply_async(put_data)
p.apply_async(get_data)

time.sleep(0.1)
q.join()