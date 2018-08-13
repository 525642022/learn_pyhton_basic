# 作者 ljc 医院
import numpy as np
import matplotlib
from numpy.random import randn

arr = np.arange(41)
print(np.sqrt(arr))
print(np.exp(arr))
##通用函数
x = randn(8)
y = randn(8)
print(x)
print(y)
np.maximum(x, y)
print(np.modf(x))


##np数据表达式 向量哈的处理向量化处理为优先化处理

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
print(xs)
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)


# 逻辑表达为数组运算 where 根据条件生成相应的
xarr = np.array([1, 2, 3, 4])
print(xarr)
yarr = np.array([2, 4, 6, 8])
carr = np.array([True, False, True, False])
result = np.where(carr, xarr, yarr)
from  numpy.linalg import  inv,qr
print(result)
X=randn(5,5)
mat=X.T.dot(X)
print(inv(mat))
res=mat.dot(inv(mat))
print(res)
q,r=qr(mat)
print(q)
print(r)
#随机数生成




