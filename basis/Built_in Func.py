#all
print(all([])) # empty ==> true
print(all([1,0,-132]))  # 0 makes fasle
print(all([1,-2,-132]))  # 0 makes fasle

#any
print(any([])) # empty ==> false
print(any([1,0,-132]))
print(any([1,-2,-132]))
print(any((0,0,0))) # empty ==> false
#ascii
print(ascii("你好"))
# bin convert intetger <10 dc> --> 2dc
print(bin(123))
# bytearray - changable binary str
b_str=bytes("abcde",encoding="utf-8")
print(b_str.capitalize(),b_str)  # str is not changable
c_str=bytearray("abcde",encoding="utf-8")
c_str[0]=60
c_str[1]=120
print(c_str)

# callable -- ()
print(callable([]))
def test():
    x=12,
    pass
class AAA():
    def __init__(self): num=10
print(callable(test))
print(callable(AAA))
#chr -- char  <---> ord
print(chr(97))
print(ord('a'))
#dir
print(dir({}))
#divmod
print(divmod(5,2))
print(type(divmod(5,2)))
#enumerate
lst=['Spring','Summer','Fall','Winter']
print(list(enumerate(lst,start=1)))

# eval simple str expression
str="pow(2,2)"
print(eval(str))
# lamda
calc = lambda n: 3 if n<4 else n  #ternary
print(calc(5))
#filter
res = filter(lambda n: n>5, range(10))
print(type(res))  # class
for i in res:
    print(i)
#map
res2 = map(lambda n: n*n, range(10))
print(type(res2))  # class
for i in res2:
    print(i)
# functools.reduce
import functools
res3=functools.reduce(lambda x,y: x+y, range(10)) #cumulative sum
print(res3)
res4=functools.reduce(lambda x,y: x*y, range(1,10)) #cumulative product
print(res4)
#fronzenset -- unchangable set
set_a=frozenset([1,232343,32324,4321])
print(globals())
#help
help(globals)
# hex
print(hex(10))
#id - return address
print(id([]))
#min /max
print(max([1,2,4,5432]))
#pow
print(pow(3,2))   # 3^2=9
print(round(1.3212,2)) # 2dc
# slice
d=range(20)
print(d[slice(2,5)])
#zip
a=[1,2,3,4,5,6]
b=['a','b','c','d']
for i in zip(a,b):   # return as an iterator
    print(i)

# sorted
dict1={1:231,2:43,9:32,-23:1323,90:12,1:2,3:4}
print(sorted(dict1.items()))  #return as a list because of order; based on key
# sorting based on value
print(sorted(dict1.items(),key=lambda x: x[1]))
