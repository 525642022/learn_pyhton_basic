# 作者 ljc
# 充分利用cpu
# 降低
# 多进程 与 多线程
import threadpool
import time


def long_op(n):
    print('%d\n' % n)
    time.sleep(2)


pool = threadpool.ThreadPool(2)
tasks = threadpool.makeRequests(long_op, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(len(tasks))
[pool.putRequest(task) for task in tasks]
pool.wait()