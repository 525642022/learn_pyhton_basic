# 作者 ljc
names = ["ljc", "laa", ["lbb", "lmm"], "lcc", "lcc"]
print(names[0], names[2])
print(names[1:3])  # 切片
print(names[-1])  # 从右边开始数
print(names[-2:])
names[1] = "gamever"
names.append("ldd")
names.insert(2, "lff")
print(names)
# names.remove("ldd")
# del names[1]
# names.pop()  # 输入下标与上一个相同
print(names.index("lcc"))
print(names.count("lcc"))
# names1 = [1, 2, 3, 4]
# names.extend(names1)
name2 = names.copy()
names[1] = "0"
names[3][0] = "aaa"
print(names)
print(name2)
for i in names:
    print(i)
print(name2[:])