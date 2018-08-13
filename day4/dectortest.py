# 作者 ljc  装饰器联系
import  time
def dec_test(func):
    def wrapper(*args,**kwargs):
        start_time=time.time();
        func(*args,**kwargs)
        end_time=time.time();
        print("run time is %s"%(end_time-start_time))
    return wrapper
@dec_test
def test(name):
    time.sleep(3)
    print("test",name)

test("ljc")

