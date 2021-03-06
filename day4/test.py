# 作者 ljc
# 定义：装饰器 本质是函数，装饰其他函数，为其他函数添加附加功能
# 原则1：不能修改被装饰函数的源代码
# 原则2：不能修改被装饰函数的调用方式
# 只是储备
# 函数即变量
# 高阶函数 1.把一个函数名当做实参传递给另外一个函数  #         可以实现在不修改源代码的情况下 为函数添加功能
#         2.返回值中包含函数名 可以实现不修改函数的调用方式
# 嵌套函数  在一个函数的函数体内使用def的方式声明另一个函数
# 高阶函数+嵌套函数= 装饰器
def logger(x):
    print(x)
def test1():
    logger("test1")
    pass

def test2():
    logger("test2")
    pass

test1()
test2()
#给test1与test2添加记录日志功能
