# 作者 ljc
# 步骤 打开  读取 关闭
# data = open("yesterday",  encoding="utf-8").read()
# print(data)  r 可读  w 可写  a 拼接
f = open("yesterday","r", encoding="utf-8")  # 文件句柄
#只适合度小文件 lowloop
# data = f.readlines()
# for k,line in enumerate(data):
#     if k!=9:
#        print(k,line.strip())
#     else:
#         print("-------")
#print( data[5])

#f.write("北京天安门\n")
count=0;
for line in f:
    count+=1;
    if(count!=9):
         print(count,line.strip())
    else:
        print("----")
print(f.tell())
f.seek(0)
#阶段
f.truncate(10)
print(f.tell())
f.close()
