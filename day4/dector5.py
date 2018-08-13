# 作者 ljc 装饰器
import time


def log_time(time_type):
    print(time_type)
    def time1(*args,**kwargs):
        start_time = time.time()
        # func(*args,**kwargs)
        end_time = time.time()
        print("this is run time %s" % (end_time - start_time))
    return time1

@log_time(time_type="onetime")
def test1():
    time.sleep(1)
    print("test1")



test1()

