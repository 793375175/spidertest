from queue import Queue
from threading import Thread
import time

q = Queue()
def put_data():
    for i in range(10):
        print("存入队列:{}".format(i))
        q.put(i)
        time.sleep(0.1)

def get_data():
    while True:
        print("取出{}".format(q.get()))
        time.sleep(0.2)
        q.task_done()

t1 = Thread(target=put_data)
t2 = Thread(target=get_data)

# t1.setDaemon(True)
t1.start()
t2.setDaemon(True)
t2.start()


q.join()
print("结束")