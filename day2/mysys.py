# 作者 ljc
import sys
import os

# 打印环境变量
print(sys.path)
# 打印当前文件名
print(sys.argv)

a = 1
b = 2
c = 3
d = a if a > b else c
msg = "理解成"
print(msg)

print(msg.encode().decode())
