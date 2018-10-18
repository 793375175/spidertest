from queue import Queue

# 创建队列对象: 先进先出
q = Queue()

# 添加数据
q.put(10)
q.put(13)
q.put(12)

print(q.task_done())
a = q.get()
# a1 = q.get()
# a11 = q.get()
# a112 = q.get()
# 当前对象的元素的个数
print(q.qsize())
# 当前队列的未完成任务数量
print(q.unfinished_tasks)

