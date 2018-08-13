# 作者 ljc
import  socket
client=socket.socket();
client.connect(("localhost",5555))
while True:
    cmd=input(">>:").strip()
    if len(cmd)==0:
        continue
    client.send(cmd.encode())
    res=client.recv(1024)
    print(res)