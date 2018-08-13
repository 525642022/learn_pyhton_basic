# 作者 ljc
# 列表生成式 生成器与列表区别 生成器当使用时才向内存中存贮 列表直接存完
# 生成器只有在调用时才会生成列表的数据 生成器之记录当前位置 只有一个__next__()方法
#  调用next是不会给yield传智 send 调用yield并传智 唤醒生成器并传值
# 可以实现单线程下的并行效果
print([i*2 for i in range(10)])
b=(i*2 for i in range(10))

for  i in b:
    print(i)

def fib (max):
    n,a,b=0,0,1
    while n<max:
        #返回当前状态的值
        yield (b)
        a,b=b,a+b
        n=n+1
    return "done"
fib_gen=fib(10)
while True:
    try:
        x=next(fib_gen)
        print(x)
    except StopIteration as e:
        print(e.value)
        break

