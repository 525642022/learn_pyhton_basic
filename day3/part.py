# 作者 ljc

def loggger(source):
    print("from %s" % source)


loggger("test")
school = "oldboy"


def changName(name):
    global  school
    school="kkskskksks"
    print("before", name)
    name = "hahah"
    print("after", name)


# 全局变量 不可以在局部变量更改 如果要更改全局变量请添加关键词global
# 只有字符串和常亮不能再局部碧昂量中更改
name = "ljc"
changName(name);
print(name,school)
