
'''
class Foo(object):
    def __init__(self,name):
        self.name=name

f=Foo("sdf")
print(type(f))
print(type(Foo))  # Foo函数来自于type

'''

'''
# 特殊方法 创建类
def func(self):
    print('hello world')

def __init__(self,name):
    self.name=name
    print("it is init :",self.name)


Foo=type('Foo',(object,),{'func':func, '__init__':__init__})  # (object,), 是元组

f=Foo("asd")

'''


class MyType(type):
    def __init__(self,*args,**kwargs):

        print("Mytype __init__",*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print("Mytype __call__", *args, **kwargs)
        obj = self.__new__(self)
        print("obj ",obj,*args, **kwargs)
        print(self)
        self.__init__(obj,*args, **kwargs)
        return obj

    def __new__(cls, *args, **kwargs):
        print("Mytype __new__",*args,**kwargs)
        return type.__new__(cls, *args, **kwargs)

print('here...')
class Foo(object,metaclass=MyType):


    def __init__(self,name):
        self.name = name

        print("Foo __init__")

    def __new__(cls, *args, **kwargs):
        print("Foo __new__",cls, *args, **kwargs)
        return object.__new__(cls)

f = Foo("Alex")
print("f",f)
print("fname",f.name)

