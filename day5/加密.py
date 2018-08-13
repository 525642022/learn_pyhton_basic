# 作者 ljc
import  hashlib
m=hashlib.md5()
m.update(b"hello")
print(m.hexdigest())
m.update(b"It is me")
print(m.hexdigest())
m.update(b"hello world")
print(m.hexdigest())