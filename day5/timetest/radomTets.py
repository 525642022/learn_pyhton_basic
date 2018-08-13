# 作者 ljc
import  random
# print(random.random()) 随机0-1之间的浮点数
# print(random.randint(1,3)) 水机1-3
# print(random.randrange(3)) 随机0-2
# print(random.choice("sjskdak"))在后面随机早一个值 可以是字符串 元组 列表
# random.uniform(1,10)两个数之间的浮点数
# random.sample 取特定数量的字符串
# random.shuffle() 洗牌功能
checkcode=""
for i in range(4):
    current=random.randint(0,4)
    if(current%2==0):
        current1=random.randint(1,9)
    else:
        current1 = chr(random.randint(65, 90))
    checkcode+=str(current1)
print(checkcode)
