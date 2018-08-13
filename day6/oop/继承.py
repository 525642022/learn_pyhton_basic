# 作者 ljc
class  School (object):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        self.students=[];
        self.teachers=[];

    def enroll(self,stu_obj):
        print("为学员%s注册"%stu_obj.name)


class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary=salary
        self.course=course
    def tell(self):
        print(f'''
            name {self.name} 
            age {self.age}
            job {self.sex}
            salary {self.salary}
            course {self.course}
            ''')

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Teacher,self).__init__()
        super(Teacher,self).__init__(name,age,sex)
        self.stu_id=stu_id
        self.grade=grade
    def tell(self):
        print(f'''
            name {self.name} 
            age {self.age}
            job {self.sex}
            stu_id {self.stu_id}
            grade {self.grade}
            ''')



