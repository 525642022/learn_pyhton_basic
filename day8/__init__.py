# 作者 ljc
# 笔记 动态import模块
# 导入 lib 下面的aa
# model=__import__('lib.aa')
# model.aa.c()
# print(model)
#__new__先与init
#__call__  foo()()执行call方法
#__meataclass__用来定义这个类一怎样的形式被实例化
#assert断言 判断一个参数是int对某些情况进行断言
import  socket


import  importlib
aa=importlib.import_module("lib.aa")
obj=aa.c()

assert  type(object) is int
if type(object) is int:
    print("hah")
else:
    print("豆豆")

#socket 三次握手，四次断开
#所有协议的底层都是socket
#tcp/ip send,recv
#udp
#只是收发的功能不一样
#服务器端
sever = socket.socket();
sever.bind(("loaclhoost",9999))
sever.listen()
while True:
    conn,addr=sever.accept()
    while True:
        data=conn.recv(1024)#最多8192
        print(data)
        if(len(data)) :
            break
        conn.send(data.upper())
#地址簇
#AF.INET AF.INET6 AF.UNIX
#socket 协议类型
#sock.SOCKETSTREAM
#socket.SOCKETDGRAM
# client
client=socket.socket()
client.connect(("locahhost",999))
client.send(data)
