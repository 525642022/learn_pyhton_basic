# 作者 ljc
def add(a,b,f):
    return  f(a)+f(b)


res=add(-3,2,abs)
print(res)