import shelve
import datetime

d=shelve.open('shelve_test')

class Test(object):
    def __init__(self,n):
        self.n=n

t=Test(123)
t2=Test(213321321)

# key -value
#不用dump 写完直接dump
name=["michael","test"]
info={'age':22,'job':'it'}
d["test"]=name  #持久化列表
d["t1"]=t
d["t2"]=t2
d['info']=info
d['date']=datetime.datetime.now()

d.close()