# 作者 ljc
import  threading

class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n=n

    def run(self):
        print("running Task",self.n)


t1=MyThread("t1")
t2=MyThread("t2")
t1.start()
t2.start()
