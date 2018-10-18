from threading import Thread

def task(msg):
    for i in range(10):
        print(msg)

t1 = Thread(target=task,args=('线程1',))
t2 = Thread(target=task,args=('线程2',))
t1.setDaemon(True)
t1.start()
# t2.setDaemon(True)
t2.start()
t2.join()
print('主线结束')