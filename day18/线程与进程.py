# 作者 ljc
import  os
from multiprocessing import Process
print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('this is a child (%s) , ppid is (%s)' % (os.getpid() , os.getppid()))
# else:
#     print('I (%s) just' % os.getpid())

def run_proc(name):
    print('this is a child thread is %s (%s)' %(name,os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' %os.getpid())
    p = Process(target=run_proc , args=('test',))
    p.start()
    p.join()
    print('end')