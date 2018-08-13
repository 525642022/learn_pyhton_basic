# 作者 ljc
def test1():
    pass


def test2():
    return 0


def test3():
    return 1, 2, 5, "shadjks"

#默认参数 当拥有默认参后 可以不进行传递
def test4(x, y=0):
    print(x)
    print(y)
# 参数组
def test5(*args):
    print(args)
def test6(**kwargs):
    for arg in kwargs:
       print(arg)
def test7(name,**kwargs):
       print(name,kwargs)

x = test1();
y = test2();
z = test3();
# print(x, y, z)
#关键参数是不能写在位置参数前面
test4( y=3,x=0)
test4(3,0)
test5(1,2,3,4,5,6)
test5(*[1,2,4,7,8])
test6(name="ljc",age=26)
test6(**{"name1":"ljc"})
test7("haha")
