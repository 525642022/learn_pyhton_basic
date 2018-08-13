# 作者 ljc
import queue
import threading

q = queue.Queue()
for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())

q = queue.LifoQueue()
for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())


# 优先队列
class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):
        return self.priority < other.priority


q = queue.PriorityQueue()
q.put(Task(1, 'important'))
q.put(Task(10, 'normal'))
q.put(Task(100, 'lazy'))


def job(q):
    while True:
        task = q.get()
        print('test', task.description)
        q.task_done


threads = [
    threading.Thread(target=job, args=(q,))
]
for t in threads:
    t.setDaemon(True)
    t.start()
q.join()
