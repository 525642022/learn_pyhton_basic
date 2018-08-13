# 作者 ljc
import  time
def test2(func):
    print( func)
    return func

def bar():
    time.sleep(3)
    print("bar")
bar=test2(bar)
bar()