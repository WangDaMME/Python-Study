class School(object):
    def __init__(self,name,addr):
        self.name=name
        self.address=addr
        self.stu_list=[]
        self.tea_list=[]

    def enroll(self,stu_obj):
        self.stu_list.append(stu_obj)
        print("%s has been enrolled in %s School"%(stu_obj.name,self.name))

    def hire(self,teacher_obj):
        self.tea_list.append(teacher_obj)
        print("%s has been HIRED in %s School"%(teacher_obj.name,self.name))

    def fire(self,teacher_obj):
        if teacher_obj in self.stu_list:
            self.stu_list.remove(teacher_obj)
            print("%s has been Fired in %s School"%(teacher_obj.name,self.name))
        else:
            print("%s teacher does not exist!!"%teacher_obj.name)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade_year):
        super(Student,self).__init__(name,age,sex)
        self.grade_year=grade_year
        self.stu_id=stu_id
    def introduce(self):
        print('''------Info of Student---------
        My name is %s,
        %s years old,
        sex is %s,
        my student id is %d,
        in %d grade'''%(self.name,self.age,self.sex,self.stu_id,self.grade_year))

    def pay_tuitionfee(self,amount):
        print("%s has paid tuition fee $%d"%(self.name,amount))


class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary=salary
        self.course=course

    def introduce(self):
        print('''------Info of Teacher---------
        My name is %s,
        %s years old,
        sex is %s,
        my salary id is %d
        I am teaching [%s],'''%(self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print("%s is teaching %s"%(self.name,self.course))


# Instantiate
school=School("Hope","countryside")
s1=Student("Liudehua",22,"m",1001,1)
s2=Student("Zhangxueyou",34,"m",1002,2)
s1.introduce()
s2.introduce()

t1=Teacher("AAA",44,"F",20000,"Math")
t2=Teacher("BBB",60,"M",3000,"Behavior Arts")
t2.introduce()

school.enroll(s1)
school.enroll(s2)

school.hire(t1)
school.hire(t2)
t3=Teacher("CCC",80,"M",500,"EDM-DJ")
print("Fire Em")
#school.fire(t2)
school.fire(t3)

# Teaching
#school.tea_list[1].teach()
print("--------The school is re-open-----")

for teacher in school.tea_list:
    teacher.teach()

school.stu_list[0].pay_tuitionfee(1000)