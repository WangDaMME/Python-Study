'''
# Decorator
import time

def timmer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        func()
        end_time=time.time()
        print("The Decorator is on, time diff: ", (end_time-start_time))
    return wrapper

@timmer
def test1():
    time.sleep(3)
    print("This is the Test1!")

#print("pure test1")
#test1()

print("Decorator is ONNN")
test1()

'''


''''
# nested function

x=0
def grandpa():
    x=1
    def father():
        x=2
        def son():
            x=3
            print(x)
        son()
    father()


grandpa()
'''
import time

# No variable - Type
def deco(func):
    def wrapper():
        start_time=time.time()
        func()
        end_time=time.time()
        print("The deco is operation with time: ", (end_time-start_time))
    return wrapper   #return wrapper's address to deco --> then the result of deco is address of wrapper .... deco() is the application ofwrapper

@deco    #synatic candy 语法糖  ie. test=deco(test)
def test():
    time.sleep(3)
    print("Test is good!")

test()





