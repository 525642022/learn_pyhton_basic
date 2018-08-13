# 作者 ljc
user, passwd = "ljc", "123"


def dec_login(login_type):
    print("longtype",login_type)
    def outer_wapper(func):
        def wrapper(*args, **kwargs):
            print("ss",*args,**kwargs)
            username = input("please input name")
            password = input("please input password")
            if user == username and passwd == password:
                print("登录成功")
                res = func(*args, **kwargs)
                return res
            else:
                exit("退出登录")
        return wrapper
    return outer_wapper


def index():
    print("welcome index")

@dec_login(login_type="home")
def home():
    print("welcome home")
    return "from home"


@dec_login(login_type="bbs")
def bbs():
    print("welcome bbs")


index()
print(home())
bbs()
