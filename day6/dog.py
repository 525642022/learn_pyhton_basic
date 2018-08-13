# 作者 ljc
class Dog:
    def __init__(self,name):
        self.name=name
    def bulk(self):
        print("%s wang wang wang " %self.name)


d1 = Dog("hh")
d2 = Dog("aa")
d3 = Dog("bb")
d1.bulk()
d2.bulk()
d3.bulk()