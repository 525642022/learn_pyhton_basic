# 作者 ljc
# set 集合关系测试 去取重复
list1 = [1, 2, 3, 4, 1, 2, 5, 6]
list1 = set(list1)
print(list1, type(list1))
list2 = set([2, 6, 0, 66, 22, 7])
print(list2)
# 两个集合去交集
print(list1.intersection(list2))
#求并级
print(list1.union(list2))
#求差集合 1里面有2里面没有
print(list1.difference(list2))
list3 = set([1,2,3])
#求字迹
print(list3.issubset(list1))

#qiu腹肌
print(list1.issuperset(list2))
#反向茶几 去合集并去除重复的
print(list1.symmetric_difference(list2))
#如果没有交集测返回true
print(list1.isdisjoint(list2))
#使用运算符
#交集
print(list1 & list2)
#并集
print(list1 | list2)
#茶几
print(list1 -list2)
#对称茶几
print(list1 ^ list2)
# subset and  upperset
#print(list)
list1.add(999)
list1.update([888,777,666])
list1.discard(11111111)