'''

def test1(*args):
    print(args)
test1(1,2,3,4,5,5)

def test2(**kwargs):   #key-value
    print(kwargs)
test2(name='kevin',age=18,sex='F')

'''

# global variable

'''
school="nottingham"


def change_name(name):
    global school
    print("Before change -->", school)
    school="Rice Uni"
    print("After change -->", school)

change_name(school)


'''

# High-Order Func

def Abs_Add(x,y,f):
    return f(x)+f(y)

print(Abs_Add(1,-6,abs))   #absolute =7
