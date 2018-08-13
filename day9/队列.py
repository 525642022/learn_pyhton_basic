# 作者 ljc
# 这张桌子
import numpy as np


def pythonsun(n):
    a = range(n)
    b = range(n)
    c = []
    print(a, b)
    for i in range(len(a)):
        a[i] = a[i] ** 2
        b[i] = a[i] ** 3
        c.append(a[i] + b[i])
    return c


def npsum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c


import sys
from datetime import datetime

size = 1000
start = datetime.now()
c = npsum(size)
delta = datetime.now() - start
print("时间", delta)

a = np.arange(5)
print(a.dtype)
print(a)
print(a.shape)

m = np.array([np.arange(2), np.arange(2)])
print(m)
print(m.dtype)
print(m.shape)

print(np.zeros(10))
print(np.zeros((3, 6)))
print(np.empty((2, 3, 2)))
print(np.arange(15))
# 数组间的运算
arr = np.array([[1, 2, 3], [2, 3, 4]])
print(arr)
print(arr * arr)
print(arr ** 0.5)
# 以为数组的切片
a = np.arange(9)
print(a[3:7])
print(a[:7:2])
print(a[::-1])
s = slice(3, 7, 2)  # 3:7:2
print(a[s])
s = slice(None, None, -1)
print(a[s])
b = np.arange(24).reshape(2, 3, 4)
print(b.shape)
print(b)
# 维度 行 列 间隔元素 -1表示反向
print(b[0,0,0])
print(b[:,0,0])
print(b[0])
print(b[0,:,:])
print(b[0,...])
print(b[0,1])
#花式索引
arr=np.empty((8,4))
for i in range(8):
    arr[i]=i

print(arr)
#返回的是一个以为数组
print(arr[[4,3,0,6]])
print(arr[[-1,-2,2,-5]])

#数组的组合
a=np.arange(9).reshape(3,3)

b=2*a

print(b)
#水平组合
print(np.hstack((a,b)))
print(np.concatenate((a,b),axis=1))
#数值组合
print(np.vstack((a,b)))
print(np.concatenate((a,b),axis=0))
#深度组合
print(np.dstack((a,b)))
#割分
a=np.arange(9).reshape(3,3)
print(a)
print(np.hsplit(a,3))
print(np.split(a,3,axis=1))
print(np.vsplit(a,3))
print(np.split(a,3,axis=0))
