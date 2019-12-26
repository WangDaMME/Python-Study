import random
print(random.random()) # 随机 0~1float浮点数
print("uniform",random.uniform(1,10))  # 指定区间 浮点数
print(random.randint(1,3))  # 随机整数 [a,b] 闭区间
print(random.randint(1,3))  # 随机整数 [a,b] 闭区间
print(random.randint(1,3))  # 随机整数 [a,b] 闭区间

#help(random.randrange)  # int 整形随机， 顾头不顾尾，
print(random.randrange(1,3))  # 就不包含3
print(random.choice('suijizhao'))# 放序列类型，str list tuple
print(random.choice((1,3,23,42,54)))# tuple随机找一个
print(random.sample('hello',3))  # 随机取三维
l=[1,2,3,4,5] # 有序列表，ordered list
random.shuffle(l)
print(l)   # 会把 原列表给混了

# Generate random verification code - 4 digits
'''
verif_code=''
for i in range(4):
    verif_code+=str(random.randint(0,9))
print(verif_code)
'''
verif_code=''
for i in range(4):
    # number
    current=random.randrange(0,4)
    # alphabet
    if i==current:
        tmp=chr(random.randint(65,90))
    #num
    else:
        tmp=random.randint(0,9)
    verif_code+=str(tmp)

print(verif_code)