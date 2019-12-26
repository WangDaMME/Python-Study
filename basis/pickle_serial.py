import pickle

def sayhi(name):
    print('hello',name)

f=open('pickle_test.txt','wb')  # pickle converts to byte stream
info= {
    'name':'Michael',
    'age': 22,
    'sex': 'M',
    'func': sayhi
}
f.write(pickle.dumps(info))
# pickle.dump(info,f) # 不用写write 和一模一样

f.close()