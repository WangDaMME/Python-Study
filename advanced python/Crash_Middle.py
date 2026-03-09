'''
1. decorator: @ - 用一个函数/类去包装另一个函数/类。
常见用途： 打日志， 权限校验，缓存，计时，把普通方法变成 property / classmethod / staticmethod
【本质】：函数 -> 返回一个新的函数 -> 替换原函数
'''
# *args： 表示 任意数量的位置参数， args 实际上是一个 tuple
# **kwargs： 表示 任意数量的关键字参数 ，是 dictionary #* 的作用是 把多个参数打包（pack）或拆包（unpack）。
# 会被 *args 收集成一个 tuple - tuple 拆包unpacking
# **kwargs = collect keyword arguments - 字典拆包

def log(func):
    def wrapper(*args, **kwargs): #
        print(f"calling {func.__name__}")
        return func(*args, **kwargs) # 调用原始函数 把结果 返回给wrapper 函数
    # 如果不写 log(add) 返回 None， NoneType' object is not callable - 要返回一个 callable 函数
    return wrapper
    #  #return wrapper's address to deco --> then the result of deco is address of wrapper .... deco() is the application ofwrapper

@log
def add(a, b):
    return a + b

print(add(1, 2))

'''
1. @property，@x.setter @x.deleter 语法糖
----》 @property 是把方法伪装成属性访问，用来做 封装 + 校验 + 兼容性设计。

#=======> 普通写法
class Person:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, value):
        if value < 0:
            raise ValueError("age cannot be negative")
        self._age = value
p = Person(18)
print(p.get_age())
p.set_age(20)
'''
''''''

#property 写法 ： @property 是把方法伪装成属性访问，用来做 封装 + 校验 + 兼容性设计。
class Person:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value
    @age.deleter
    def age(self):
        del self._age

p = Person(18)
print(p.age) # 不用get
p.age = 25
print(p.age) # 25

'''
3. reflection 反射
反射就是：运行时动态查看 / 获取 / 修改对象的信息。
常用于： 动态调用方法，配置驱动开发，ORM / 框架底层，插件系统

Python 反射 = 简单说 就是用字符串操作对象，obj.x 等价于 getattr(obj, "x")
4 个核心函数
hasattr   判断有没有
getattr   获取
setattr   设置
delattr   删除
'''
class Dog:
    def __init__(self,name):
        self.name = name
    def eat(self, food):
        print(self.name, "is eating", food)

# 1. 检查属性方法
d = Dog("xiaogou")
print(hasattr(d, 'eat'))
print(hasattr(d, 'name')) #


# 2 获取属性
print(getattr(d, "name"))   # xiaogou
func = getattr(d, "eat") # 获取方法
func("bone")

# 4 设置新属性
setattr(d, "age", 3)
print(d.age)           # 3

# 实现route handler
class Handler:
    def login(self):
        print("login")
    def logout(self):
        print("logout")
    def home(self):
        print("home")
h = Handler()
cmd = input("command : ").strip()
if hasattr(h,cmd):
    func = getattr(h,cmd)
    func()
else:
    print("no such command")





'''
4. Mixin 拼装功能
是给别的类“混入”一些能力。
通常很小,只做一件事,常配合多继承使用,不单独实例化
'''
class JsonMixin:
    def to_dict(self):
        return self.__dict__

class Person(JsonMixin):
    def __init__(self, name, age):
        self._age = age
        self.name = name

p = Person("xiaogou", 18)
print(p.to_dict())

'''
5. class Foo(object, metaclass=MyType): 里的 metaclass 是什么？
metaclass 是“创建类的类”。普通类创建对象；元类创建类。
Python 中大多数类都是 type 创建出来的。
metaclass 可以干什么？

它可以在“类创建的时候”拦截并修改类。强制类规范,自动注册类,给类加属性/方法
'''
class MyType(type):
    def __new__(cls, name, bases, attrs):
        attrs['added_attr'] = "hello from metaclass"
        return super().__new__(cls, name, bases, attrs)
class Foo(metaclass=MyType):
    pass

print(Foo.added_attr)

'''
6. function 作为值传递
'''
def add(a, b):
    return a + b
def compute(func, a, b):
    return func(a, b)
print(compute(add, 3, 4))


'''
7. classmethod / staticmethod / 实例方法区别
实例方法：第一个参数是 self，操作对象实例

类方法：第一个参数是 cls，操作类本身

静态方法：啥都不自动传，只是逻辑上放类里
'''
class A:
    x = 100 # class_attr

    def instance_method(self):
        print("instance", self.x)

    @classmethod
    def class_method(cls): # pass cls
        print("class", cls.x)

    @staticmethod
    def static_method():
        print("static")
A.static_method()
a = A()
a.static_method()
a.instance_method()
A.class_method()

'''
8. iterator 迭代器 __iter__ 和 __next__方法
'''
class Count:
    def __init__(self, n):
        self._n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self._n:
            raise StopIteration
        self.current += 1
        return self.current
counter = Count(5)
for i in counter:
    print(i)


'''
8. generator 生成器 yield 关键字 - lazy evaluation 惰性计算
只有在需要的时候才计算下一个值，而不是一次全部计算出来。一次性计算 1亿个占用巨大内存很慢
主要：省内存（最重要），处理大数据
'''
def count(n):
    i = 1
    while i <= n:
        yield i
        i+=1
for x in count(5):
    print("gen",x) #<generator object count at 0x100e1bf90>


# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a  # 先返回0
#         a, b = b, a + b
#
# /with/yield/del

#https://github.com/WangDaMME/Python-Study/blob/master/basis/list.py 深浅copy

# module

# linkedlist 结构

# parallel concurrency https://github.com/WangDaMME/Python-Study/blob/master/basis/parallel%20concurrency.py
