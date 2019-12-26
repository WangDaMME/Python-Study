'''
# list generator
list = [i*2 for i in range(10)]
print(list)
# [Func(i)]   -- 传函数

'''

'''
# Organized Generator   -----  list
g = (i*2 for i in range(1000))
print(type(g))
print(g.__next__())
print(g.__next__())
print(g.__next__())
'''
'''
def fib(max):
    a,b,n=0,1,0
    while (n < max):
        print(b)
        a, b = b, a+b
        n+=1
    return "done"

fib(8)
'''

# yield Generator
def fib(max):
    a,b,n=0,1,0
    while (n < max):
        yield b
        a, b = b, a+b
        n+=1
    return "done"

#f=fib(8)
'''
for i in f:
    print(i)

fib(8)
'''

# Capture the Exception Fault
g=fib(8)
while True:
    try:
        x=next(g)
        print('g',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break





