# 作者 ljc
import time


def test1(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print("the run time is %s" % (end_time - start_time))


def bar():
    time.sleep(3)
    print("bar")


test1(bar)
