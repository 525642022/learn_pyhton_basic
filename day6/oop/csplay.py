
# 作者 ljc
# class Role:
#     def __init__(self,name,role):
#         self.name=name
#         self.role=role
#     def shoot(self):
#         print("%S shoot"%(self.name))
#     def buyGun(self ,gunname):
#         print("%s bug gun %s"%(self.name,gunname))
#     def __del__(self):
#         print("%s彻底死了"%self.name)
#
# r1=Role("ljc","police")
# r2=Role("ljc1","Nopolice")
# r1.buyGun("ak")
# r2.buyGun("ss")

class People(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Relation(object):
    def makeFriend(self,obj):
        print(self.name,obj.name)

class Man(People,Relation):
    def piao(self):
        print("paio")

m=Man("ljc","23")
m1=Man("ljc1","24")
m.piao()
m.makeFriend(m1)


