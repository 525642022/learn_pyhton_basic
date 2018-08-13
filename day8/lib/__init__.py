# 作者 ljc
#socketserver 是在socket基础上对网络层面上进行封装
#BaseServer
# 创建一个请求处理类，并且这个类要继承BaseRequestHandler，并且重写Handler方法
# 你必须实例化 TCOServer 并传递server ip和你上面的请求处理类个这个TCPServer
# sever.handleRequest 只处理一个请求
# server.serve_forver 处理多个请求
import socket
