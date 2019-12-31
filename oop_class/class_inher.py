#class People:   #classic class经典类
class People(object):  #新式类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print("%s is eating"%self.name)
    def sleep(self):
        print("%s is sleeping"%self.name)

class Relationship(object):
    #def __init__(self,n1,n2):
    def __init__(self,n1,n2):
        print(self.name)  # 因为 init最先执行 看看 传没传进来name
    def make_friends(self,obj):  # obj 对象
        print("%s is making friends with %s"%(self.name,obj.name))
        #???Obj 为什么能找到.name???
        # 多继承（父1，父2）-- 子类已经继承了父1，父2 就可以共享 父1的信息了。
        #  如果子类 有对该变量 初始化，self._init 直接 用子类的信息了，也能共享
        # 而且从左往右找的，# 如果  Relationship，People 顺序



#Inheritance
class Man(People,Relationship):
    def __init__(self,name,age,man_hormone=10):
        #People.__init__(self,name,age)# 经典类写法
        super(Man,self).__init__(name,age)  # 新式类
        # super写法 稍好一点: 1.People 类名改了，之后子类都要改  2. 多继承时
        self.man_hormone=man_hormone
    def sleep(self):
        People.sleep(self)  # reconstitute
        #print("MANNNN is sleeeping",self.name)  # overwrite
    def show_hormone(self):
        print("%s 's hormone is %s"%(self.name,self.man_hormone))

class Woman(Relationship,People):
    def give_birth(self):
        print("%s gives birth",self.name)
m1=Man("Mike",22)
#m1.sleep()
#m1.show_hormone()
w1=Woman("QQQueen",44)
m1.make_friends(w1)
w1.make_friends(m1)