# 作者 ljc
import threading
import  time
event = threading.Event()
def lighter():
    count=0
    event.set()
    while True:
        if count>5 and  count<10:#改成红绿灯
            event.clear()#清空标志位
            print("改成红灯了")
        elif count>10:
            event.set()#
            print("绿灯")
            count=0
        else:
            print("绿灯")
        time.sleep(1)
        print(count)
        count+=1
def car(name):
    while True:
        if(event.is_set()):# 代表绿灯
            print("%s is running" %name)
            time.sleep(1)
        else :
            print("%s sees red light waiting" %name)
            event.wait()
            print("start going")

light=threading.Thread(target=lighter,)
light.start()
car1=threading.Thread(target=car,args=("ljc",))
car1.start()