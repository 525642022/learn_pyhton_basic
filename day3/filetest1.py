# 作者 ljc
f=open("yesterday", "r+", encoding="utf-8")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.write("-----------ss---------")
print(f.readline())
