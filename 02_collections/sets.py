#sets are mutable but unordered collections 

a={14,2,4,5,6,3,2}
print(a)

#repeated items are excluded from set 

#common items can be collected using sets because if there is anything common eg:

b={2,5,8}

common_items=a and b

d={'n','o','i','r'}
e={'o','i'}
print(common_items)

union=d | e
print("union is :",union)

symmetric_difference=d.symmetric_difference(e)
print("Symmetric Difference is",symmetric_difference)

common=d & e
print("common is",common)

common1="".join(sorted(common))
print(common1)


#add elements in a set 

b.add(12)
print(b)

b.update([4,6,5])
print(b)


x=b.pop()
print(x)

e={}
print(type(e))

f=set()
print(type(f))

#we cannot create empty set just by e={} this is like dictionery so instead



