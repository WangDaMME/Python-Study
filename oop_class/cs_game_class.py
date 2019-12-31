
class Role(object):
    # class variable
    n=123
    name="This is the class variable"
    n_list=[]
    def __init__(self,name,role,weapon,life_value=100,money=15000): # default para
        #实例变量 object variable  实例变量( 静态属性，作用域就是实例本身)
        self.name=name
        self.role=role
        self.weapon=weapon
        self.life_value=life_value
        self.money=money

    def shot(self):  #动态属性--类的方法
        print("%s Shoot use %s"%(self.name,self.weapon))


r1=Role('Jack','police','b46') #实例化
r1.name='KOBE'
# Add attribute
r1.bullet_proof=True  # 新加属性 r2是没有的
r1.shot()
print(Role.n,Role.name)
print(r1.name,r1.bullet_proof)   # 类变量 和 实例变量，先找 实例变量

#删掉一个属性
print(r1.weapon)
del r1.weapon
# print(r1.weapon)

# 通过实例 改类 变量 改不了
r1.n="change class variable" # 相当于 自己加了个属性
print("r1",r1.n)
r2=Role("Axsl","terrorist","b22")
print("r2",r2.n)
print("Role",Role.n)

Role.n='ABC'
print("r1",r1.n)
print("r2",r2.n)
print("Role",Role.n)

# 类 列表变量  --》 同用一个内存地址
r1.n_list.append("from r1")
print("r1",r1.n_list)
r2.n_list.append("from r2")
print("r2",r2.n_list)
print("Role list",Role.n_list)