list1=[1,3,5,7,9,2,4]
set1=set(list1)
print(set1,type(set1))

set2=set([1,6,7,3,5,7,0,9,8])
print(set2)

union_set=set1.union(set2)
print("Union",union_set)
intersection_set=set1.intersection(set2)
print("Intersection",intersection_set)
diff_set=set1.difference(set2)   #in 1 not in 2
print("Difference",diff_set)
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.symmetric_difference(set2))

set1.remove(12)
print(set1)
set1.discard(12)
print(set1)