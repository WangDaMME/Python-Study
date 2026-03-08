# =============== Python Crash =============== #

'''
1. 基本语法结构
'''
def check(x):
    if x > 10:
        print(x)  # 不用；
    elif x ==10:
        print(str(x) +"0sss") #elif
    else :
        print(str(x*-1))
check(10)
# 三元表达式
print("big" if 10> 5 else "small")

# for , while
for i in range(1,11):
    if i<5:
        continue
    print(i)
i= 0
while(i<5):
    if i ==3:
        break
    print("this is while %d"%i)
    i+=1

#enumerate , zip
arr = [10, 20, 30]
for k,v in enumerate(arr):
    print(k,",",v)

#2. list 语法
# arr[5]= '20';  # index out of range
# print(arr)

arr.append(40)
print(arr[3])
print(arr.pop()) #删除最后一位
print(arr.pop(1)) # 删除第二位

arr = [0,1,2,3,4]

print(arr[1:3])  # [1,2] 钱包后不包
print(arr[:3])   # [0,1,2]
print("去掉最后一个",arr[:-1])   # [0,1,2 ,3]
print(arr[-1])   # 4
print(arr[-2:]) # 取后2 位
print(arr[::-1]) # 反转数组
print(arr[::-2]) # 从后往前，每隔 2 个取一个元素。
#:: 是 Python 切片 (slicing) 语法的一部分，用于指定 步长 (step)。 start end step
# sequence[start : end : step], ::step 就是从头到尾
print("slice",arr[::2])
print(arr[1:3:])

two_d_arr=arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(two_d_arr[0][1])

# 列表推导式list comprehension
# 1. [expression for item in iterable if condition]
# 2。 [expr1 if condition else expr2 for x in nums]
#1.1 传统写法
nums = [1,2,3,4,5]

result = []
for x in nums:
    result.append(x*x)

print(result)
#1.2
result2 = [x*x if x % 2==0 else -1*x for x in nums] #偶数平方
print(result2)

# tuple Immutable
tuple1 = (1,'a',True)
# tuple1[1]='xxxx' # TypeError: 'tuple' object does not support item assignment
for item in tuple1:
    print(item)

# zip 用法
a1 = [1,2,3] #用来 把多个可迭代对象按位置配对 (pair)。打包成 tuple （immutable 不可以修改）
b1 = ['a','b','c','d'] # 1.长度不同， zip 会按最短的 iterable 停止
#zip 是 iterator（迭代器），只能用一次。
# x,y = zip(*result) # ValueError: not enough values to unpack; 因为 result 现在是 空 iterator。
result = list(zip(a1,b1))
print(result)
x,y = zip(*result)
print("unzip a",x)


# unzip ie. unpacking
pairs = [(1,'a'),(2,'b'),(3,'c')]
x1, y1 = zip(*pairs)
print("unpacking", x1, y1)
print("isintance", isinstance(x1, tuple)) # True
x1_convert = list(x1)
print("isintance", isinstance(x1_convert, tuple), x1_convert) # True


a = [1,5,3]
b = [4,2,6]

result = [max(x,y) for x,y in zip(a,b)]
print(result)

print("============== array iter function ===========")
nums=[1,2,3,4,5]
# 1.没有 foreach 利用 map/filter ( lambda:函数)
# sorted(), any(), all(), sum(), max(), min(), len(), reversed()
print(sorted(nums, reverse=True))
print(sorted(nums, key=abs)) #用 key function。
# sorted(list, key=lambda x: x.age) == Collections.sort(list, (a,b)->a.age-b.age);
people = [
    ("Tom",25),
    ("Alice",20),
    ("Bob",25)
]
# 这里的 (x[1], x[0]) 确实是一个 tuple，Python 用它来实现 多条件排序（multi-key sorting）。
print(sorted(people, key = lambda x: (x[1],x[0]))) #先age 再name
# print(any(nums, key = lambda x: x==4))  -- any 没有key 参数
# print(any(x==4 for x in nums)) # 不如 for 循环check一下 early return
### 非要implemnt comparetor
# from functools import cmp_to_key
#
# def compare(a,b):
#     return a-b
#
# sorted(nums, key=cmp_to_key(compare))
### 非要implemnt comparetor
print(list(reversed(nums)))

# map 转换类/filter/reduce/flatten
print("!!! 核心参数", "{func, iterable=}, 返回map iterator ")
print("!!! 以built in function为例", "{len, iterable=nums=['apple', 'ok']}") #[5,2]

map_res1 = map(lambda x: x*x, nums) # [x*x for x in nums]
# 查看iterator
print(next(map_res1))
print(next(map_res1))
print( "map_res1", list(map_res1)) # [9, 16, 25] 查看即消耗

pairs = [(1,3),(2,1),(4,2)]

print(sorted(pairs, key = lambda x: x[1])) #按第二个元素排

# lambda 匿名函数
print("!!! lambda 核心参数", "参数：表达式, lambda x: x+1;   " \
                             "\n lambda x,y: x+y;")

nums=[1,2,3,4,5]
from functools import reduce
reduce_res = reduce(lambda a,b: a+b, nums)
print(reduce_res)
matrix = [[1,2],[3,4],[5,6]]
from itertools import chain
flat = list(chain.from_iterable(matrix))
print("flat", flat)

nums=[1,1,2,2,3]
from collections import Counter
print("counter",Counter(nums))

add = lambda x,y : x+y
print(add(3,4))

print("==============dict / set / defaultdict ===========")
d = {"a":1,"b":2,"c":3}
# 1. 遍历key
for k in d: #或者显示写法 d.keys()
    print(k,d[k])
print("keys:", d.keys())

for v in d.values():
    print(v)
for k,v in d.items():
    print("item:" , k,v)
print("同时 拿 index")
for i, (k,v) in enumerate(d.items()):
    print(i,k,v)
print("--> dict comprehension")
result = { k:v*2 for k,v in d.items()} # {} dict 类型
print(result,"<----")
#按value 排序
# 为什么是x【1]: 返回每个元素 tuples [("a",3), ("b",1), ("c",2)]
sorted_d = sorted(d.items(), key= lambda x: x[1])
print("sorted_d", sorted_d)


print("========== default dict ==============")

# defaultdict 字典增加版 - 当 key 不存在时，自动创建默认值
# 普通dict
d = {}
nums = [1,2,1]
for x in nums:
    if x not in d:
        d[x] = 0
    d[x] += 1 # 否则没有元素报错
print("normal dict", d)

from collections import defaultdict
# defaultdict(default_factory)
# default_factory	一个 可调用对象 (callable)，用于生成默认值； 默认值生成函数
# ie. 当 key 不存在时，调用int 生成默认函数
d = defaultdict(int)

for x in nums:
    d[x]+=1
print("default dict", d)
print("default dict", d[13213124]) #不存在的
print("default dict", d[1]) #不存在的


print("========== set ==============") # set 是无序的
s1= {1,2,3} #按这种dict 定义 就是去重
s1.add(1) # set.remove
print("set keys", s1) # set keys {1, 2, 3}
#或者
nums = [4,5,6]
s2 = set(nums)
print("set", s2) # set keys {1, 2, 3}

print("union", s1 | s2)
print("intersection", s1 & s2) # 或者 s1- s2
#set 不能放 mutable 类型，
# s = {[1,2]} #: unhashable type: 'list'
#因为 set 只能放 hashable 类型：int， str，tuple
'''set顺序不保证'''
# for i, x in enumerate(s1):
#     print(i, x)

# set 也可以放 object 改写equals object 可以像 Java 一样改写 equals
''' set object
__eq__()
__hash__()
'''
class Person:
    def __init__(self,name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
    def __hash__(self):
        return hash(self.name)
jordan = Person("jordan")
michaelbjordan = Person("jordan")
p_set = {jordan, michaelbjordan}
print(len(p_set)) #1


# 问题 1.map set heap swich case global tuple
# 2. 语法糖
# deque，deque，Counter， defaultdict

# https: // github.com / WangDaMME / Python - Study
# https: // github.com / WangDaMME / DataStructure - Algorithm / tree / master / adt

# 2d array

