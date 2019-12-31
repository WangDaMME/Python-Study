# special internal method

class Animal(object):
    ''' This describes the Animal class'''
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def __call__(self, *args, **kwargs):
        print('__call__ is called')

    def __str__(self):
        return "an Animal class"

    def __getitem__(self, key):
        print('_getitem',key)

    def __setitem__(self, key, value):
        print('_setitem',key,value)

    def __delitem__(self, key):
        print('_delitem',key)



print(Animal.__doc__)
a=Animal("sss",12)
a()
Animal("sss",12)()
print(a)
print(Animal.__dict__)   # res: an Animal class
print(a.__dict__)


b=Animal("dddd",321)
a['var1']='wwww'     # 自动触发 set
res=a['var1']        # 自动触发get
del a['var1']        # 自动触发 del