# Mixin: 
# 是一种“功能模块类”，用来给别的类“混入”某种功能
# 不单独实例化，只提供方法， 不负责完整业务逻辑，通过多继承组合进别的类

class DictMixin:
    def to_dict(self):
        return self.__dict__ # 将实例的属性以字典形式返回
    
class User(DictMixin): # 继承mixin
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Alice", 30)
print(user.to_dict()) # 输出: {'name': 'Alice', 'age': 30

#write a class DictMixin(TO_DICT) and a class pYTHON jSONMIXIN (CONTAINS TO_JSON) FUNCTIONS, 
# And there is MyClass(DictMixin, JSONMIXIN) init(name,data, secreate), 
# MyClass1(DictMixin) init(name,data, secret), MyClass2(JSONMIXIN) init(name,data, secreate) IN python,

import json

class DictMixin:
    def to_dict(self):
        return {
            k:v for k, v in self.__dict__.items() if not k.startswith('_')
        }
        # return dict(self.__dict__) # 将实例的属性以字典形式返回 - self.__dict__： 真正存储对象数据的地方的一个 饮用
        # dict(self.__dict__)： 浅拷贝， 不影响原对象 将 __dict__ 转换为一个新的字典对象，避免外部修改原始的 __dict__ 导致对象状态不一致

class JsonMixin:
    def to_json(self):
        if hasattr(self, 'to_dict'):
            data = self.to_dict() # 获取字典表示
        else:
            data = {
                k:v for k, v in self.__dict__.items() if not k.startswith('_')
            }
        try:
            return json.dumps(data) # 转换为 JSON 字符串
        except TypeError as e:
            raise ValueError(f"对象包含不可序列化的属性: {e}")
        
class MyClass(DictMixin, JsonMixin):
    def __init__(self, name, data, secret):
        self.name = name
        self.data = data
        self._secret = secret

class MyClass1(DictMixin):
    def __init__(self, name, data, secret):
        self.name = name
        self.data = data
        self._secret = secret
        self._cache = "cache data"

class MyClass2(JsonMixin):
    def __init__(self, name, data, secret):
        self.name = name
        self.data = data
        self._secret = secret
        self._cache = "cache data"