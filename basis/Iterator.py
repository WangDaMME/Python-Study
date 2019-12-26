'''
from collections.abc import Iterable
# Iterable -- can be put in for loop
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((12,23,45,65),Iterable)) # tuple
print(isinstance(set([]),Iterable)) # set
print('Int',isinstance(12,Iterable)) #int
print('Generator',isinstance((2*i for i in range(5)),Iterable)) #list generator

print(dir([]))

'''

'''
# Iterator - contains __NEXT__ func
from collections.abc import Iterator
print(isinstance([],Iterator))
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))
print(isinstance((12,23,45,65),Iterator)) # tuple
print(isinstance(set([]),Iterator)) # set
print('Int',isinstance(12,Iterator)) #int
print('Generator',isinstance((2*i for i in range(5)),Iterator)) #generator

#print(dir(2*i for i in range(5)))
'''


from collections.abc import Iterator

# Use iter() func convert
print("Convert using 'iter()'")
print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter('abc'),Iterator))
print(isinstance(iter((12,23,45,65)),Iterator)) # tuple
print(isinstance(iter(set([])),Iterator)) # set

#print(dir(2*i for i in range(5)))