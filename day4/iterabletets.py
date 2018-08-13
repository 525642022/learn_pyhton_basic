# 作者 ljc 可以被next调用并且不断返回下一个值得对象
from collections import  Iterable
from collections import  Iterator
# 判断是否可迭代
print(isinstance((x for x in range(10)),Iterator))
print(isinstance([],Iterable))
# 迭代器
a=[1,2,3]
#生成器都是迭代器对象 list dict str是可迭代对象 但不是迭代器
#迭代器对象表示是一个数据流 迭代器可以表示一个
# 无线大的数据流但是不能能使用列表哈存储
b=iter(a)
print(next(b))
print(next(b))
#在3.0里面rang（10）就是一个迭代器

