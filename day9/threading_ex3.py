# 作者 ljc
import threading
import time


t_object=[]
lock=threading.Lock()
num=0
def run(n):
    lock.acquire()
    global  num
    num+=1
    lock.release()
start_time=time.time()
for  i in range(50):
    t=threading.Thread(target=run,args=("t_%s"%i,))
    t.start()
    t_object.append(t)

for t in t_object:
    t.join()


print("cost",num)
#最多有多少个线程在同时执行
semaphore=threading.BoundedSemaphore(5)
event=threading.Event() #线程中的标志位
event.wait()#如果没有设置标志位则一直等待 等待标志位被设定
event.clear()#清空标志位