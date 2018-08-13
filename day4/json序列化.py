# 作者 ljc json数据序列化 只dump一次 只load一次
import json
import pickle
def saHi(name):
    print("hello",name)
info={
    "name":"ljc" ,
    "age" :27 ,
}

f=open("test.txt",'w')
print(json.dumps(info))

f.write(json.dumps(info))
info["name"]="ll"
f.write(json.dumps(info))

# f.write(pickle.dumps(info)) ==pickle.dump(info,f)
f.close()
