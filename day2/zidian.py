# 作者 ljc
# 集合 字典 列表
# 字典  key-value 键值对
# 不要用 pop
info = {
    "name1": "ljc1",
    "name2": "ljc2",
    "name3": "ljc3",
}
info1 = {
    "name3": "ljcmm",
    1: 2,
    2: 3,
}
print(info.items())
info.update(info1)
print(info["name1"])
info["name1"] = "ljc0"
info["name4"] = "ljc4"
del info["name1"]
print(info)
print("name5" in info)
print(info.get("name5"))
# 初始化一个新的字典
c = dict.fromkeys([6, 7, 8], [1,{"name":"alex"},444])
c[7][1]["name"]="sex"
print(c)
#字典的循环
for i in info:
    print(i,info[i])
for k,v in  info.items():
    print(k,v)