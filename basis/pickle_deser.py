import pickle

def sayhi(name):
    print('hello2222', name)

f=open('pickle_test.txt','rb')
data=pickle.loads(f.read())
#data=pickle.load(f)
f.close()
print(data["age"])
print(data["func"]('name'))  # 只要函数名一样就能用，不是serial函数的地址，所以同名就按这本文件deser运行