'''

'''
list=['a','b','c','d','e']
print(list[-3:-1])  # 顾头不顾尾，d --- c ---（-3）b没取到

print(list[-3:0])  # 什么也取不到
print(list[-3:])
print(list[:3])   # 不顾尾

list.insert(2,"omg")
print(list)
'''

# 浅拷贝
list1=['a','b','c','d','e']
list2=list1.copy()
list1[2]="我的"
print(list1)
print(list2)

#前拷贝 套列表
list3=['a','b',['c','d'],'e']
list4=list3.copy()
list3[2][0]="我的c"
print(list3)
print(list4)


# 深拷贝
import copy
list5=['a','b','c','d','e']
#list6=copy.copy(list5)  #浅拷贝 ，跟list自带的一样
list6=copy.deepcopy(list5)  #深拷贝 ，跟list自带的一样

print(list5)
list5[2]="我的"
print(list5)

print("deep---",list6)


'''
pswd=str.maketrans('abcde','12345')
print("wang da is good".translate(pswd))