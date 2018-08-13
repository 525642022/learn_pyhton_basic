# 作者 ljc 携程效果 单线程下的并行效果
import  time
def consumer(name):
    print("%s 吃暴走" % name)
    while True:
        baozi=yield
        print("baizi[%s]来了，被[%s]吃了"%(baozi,name))
# c=consumer("ljc")
# next(c)
# b1="芥菜仙子"
# c.send(b1)
# next(c)

def producer(name):
    c=consumer("A")
    c2=consumer("B")
    next(c)
    next(c2)
    print("开始吃包子")
    for i in range(10):
        time.sleep(1)
        print("做了一个包子，分类；两个")
        c.send(i)
        c2.send(i)
producer("ljc")
