# 作者 ljc
import  time;
def dec_test1(func):
    def test_time():
        start_time=time.time()
        func();
        end_time=time.time()
        print("run time is %s" %(end_time-start_time))
    return test_time



def test1():
    time.sleep(3)
    print("test1")
test1=dec_test1(test1)
test1();