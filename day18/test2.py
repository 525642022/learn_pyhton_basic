# 作者 ljc
import time, threading


def loop():
    thread_name = threading.current_thread().name
    print("this thread name %s" % thread_name)
    n = 0;
    while n < 5:
        n = n + 1
        print('thread %s >>>>>%d' % (thread_name, n))
    print('this is end %s' % thread_name)


thread_name = threading.current_thread().name
print('thread %s is running...' % thread_name)
t = threading.Thread(target=loop, name="loopThread")
t.start()
t.join()
print('this is end %s' % thread_name)

