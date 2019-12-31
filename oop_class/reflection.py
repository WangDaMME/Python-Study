# Reflection
class Dog(object):
    def __init__(self,name):
        self.name=name

    def eat(self,food):
        print("%s is eating %s"%(self.name,food))

'''  # has get
d=Dog("WangCai")
choice1=input(">>:").strip() # 对空格 /n 截断
# attribute
print("Attribut：", hasattr(d,choice1))
# method
choice2=input(">>:").strip() # 对空格 /n 截断
print("Method：",hasattr(d,choice2) ) #(object,"str")调用类型

# getattr
print(getattr(d,choice1))   # 属性：直接把值返回
print(getattr(d,choice2))   # 方法： 返回方法内存地址 +（）：调用
getattr(d,choice2)("Potato")  # Call 调用

'''
def bark(self):
    print("%s is barking ..."% self.name)
d=Dog("WangCai")
choice=input(">>:").strip()
'''
# setattr  - method
if hasattr(d,choice):
    func = getattr(d,choice)  # 返回内存地址
    func("Set woooords")
else:
    setattr(d,choice,bark)   # bark 函数  -- 但 调用 是这个choice，就是起个什么名，实际还是调用choice
    d.talk(d)    # d.不能直接写 字符串
'''
'''
# setattr  - attribute
if hasattr(d,choice):
    value = getattr(d,choice)  # 返回值
    print(value)
else:
    setattr(d,choice,22)        # 在 x.y =v  value处 设置
    print(getattr(d,choice))    # d.不能直接写 字符串

print(d.money)  # 写死了

'''


# del attr
if hasattr(d,choice):
    delattr(d,choice)

print(d.name)