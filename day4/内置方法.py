# 作者 ljc
# abs 取绝对值
# all 列表中不包含假 返回true
print(all([1, 0, -1]))
# any 列表中有一个是真则为真
print(any([0, 1]))
# ascii
print([ascii(["a", "b", "是"])])
# bin(x) 十进制转二进制文件
print(bin(12))
# bool([x]) 判断真假
# bytearray 可修改的字节二进制格式
a = bytes("abcde", encoding="utf-8")
b = bytearray("abcde", encoding="utf-8")
print(a.capitalize(), a)
b[1] = 110;
print(b)
# callable 判断是否可以调用
print(callable(print))
# chr ascII转文字 ord 文字装ascII
print(chr(97))
print(ord("a"))
# classmethod 类方法
classmethod
# compile 实现动态导入
# py_obj=compile(code,"","exec")
# exec(py_obj)
# complex 返回负数
print(complex(10))
# dir 返回类的所有方法
# eval() 字符串变成字典
# filter() 在一组数据中过滤出想要的
# calc=lambda  n:print(n);
# calc(5)
res = filter(lambda n: n > 5, range(10))
for i in res:
    print(i)

# map()对传入的值按照前面的方式进行处理
res1 = map(lambda n: n * n, range(10))
for i in res1:
    print(i)
#reduce 按照前面的方式进行运算
import  functools
res=functools.reduce(lambda x,y:x+y,range(10))
print(res)
#frozenset 不可变的集合
a=frozenset([1,2,1,3,4])
print(a)

# getattr() 面向对象讲
# globals() 当前程序中所有的变量的集合
print(globals())
# hex() 把数字转成16进制
# locals() 打印局部的变量
def test():
    local_var=333

# pow() 但会多少次方

# repr() 用字符串表示对象

# round() 保留小数的位数
a={4:2,3:2,8:7}
print(sorted(a.items()))
# zip() 列表拼接
a=[1,2,3,4,5,6]
b=[1,2,3,4]
for i in zip(a,b):
    print(i)
