# 作者 ljc
import threading
import time


t_object=[]
lock=threading.Lock()
num=0
def run(n):
    print("task",n)
    time.sleep(2)
    print("done")
start_time=time.time()
for  i in range(50):
    t=threading.Thread(target=run,args=("t_%s"%i,))
    t.setDaemon(True)#把当前线程设置为守护线程
    t.start()
    t_object.append(t)

# for t in t_object:
#     t.join()


print("cost",time.time()-start_time)