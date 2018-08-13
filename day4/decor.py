# 作者 ljc
import time
def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time();
        print("the time is",start_time,stop_time)
        return  warpper


@timmer
def test1():
    time.sleep(3)
    print("test1")

