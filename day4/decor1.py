# 作者 ljc
def foo():
    print("foo")
    bar();
def bar():
    print("bar")
foo();

calc=lambda  x:x*3
print(calc(3))