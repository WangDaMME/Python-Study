
# staticmethod
'''
class Dog(object):
    def __init__(self,name):
        self.name=name

    @staticmethod
    def eat(obj):  # staticmethod 使下面函数跟类没什么关系了
        print("%s is eating %s"%(obj.name,"sss"))

d=Dog("WangCai")
d.eat(d)

'''

# Classmethod 类方法

'''
class Dog(object):
    name="xxxx"
    def __init__(self,name):
        self.name=name

    @classmethod
    def talk(self):
        print("%s is talking"%self.name) # 还是需要self调用

d=Dog("wjl")
d.talk()
'''

#Property 属性方法 & setter deleter函数
class Dog(object):
    def __init__(self,name):
        self.name=name
        self.__food=None  # private

    #属性方法
    @property
    def eat(self):  # 接不了参数
        #print("%s is eating %s"%(self.name)) # 还是需要self调用
        print("%s is eating %s"%(self.name,self.__food)) # 还是需要self调用

    @eat.setter
    def eat(self,food):
        print("set to food")
        self.__food=food  # 通过外部 设置私有属性

    @eat.deleter
    def eat(self):
        del self.__food
        print("Done deleting")

d=Dog("wjl")
# d.eat()   # 返回一个属性，不是方法
d.eat="Hamburger"  # 外部把 hambuerger --》eat.setter -->私有self.__food --> property eat函数
d.eat       # 属性 值=None， 内部方法也会实现
#delete
#del d.name   # 正常的成员变量 是可以删除的  <==> 传进的私有变量 你都找不着，要借用deleter函数
#print(d.name)
del d.eat
