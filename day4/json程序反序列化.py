# 作者 ljc
import  json
import pickle
def saHi(name):
    print("hello2",name)

f=open("test.txt","r")
data=json.loads(f.read())
# data=pickle.loads(f.read())==pickle.load(f)

f.close()
print(data)

