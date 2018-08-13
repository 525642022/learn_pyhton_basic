# 作者 ljc
import socket
import os
server=socket.socket()
server.bind(("localhost",5555))
server.listen(5)
while True:
    conn,addr=server.accept()
    print("new coonn:",addr)
    while True:
        data=conn.recv(1024)
        if not data:
            print("客户端断开")
            break
        print("接受到数据",data)
        res1 = data.upper()
        res = os.popen(data.decode()).read()  # 接受字符串，执行结果也是字符串
        if len(res)==0:
            res="cmd has not output"
        print(res)
        conn.send(res.encode("utf-8"))