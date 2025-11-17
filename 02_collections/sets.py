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

#discard vs remove 
#discard removes without error which means if there is no element it doesnt return error but remove does
#pop removes  returns a random element 
#del deletes the entire set
#clear() clears the set elements




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

#we cannot create empty set just by e={} this is like dictionary so instead

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities.intersection_update(cities2)
print(cities)

'''
intersection_update(other_set) modifies the original set (cities) so that it only keeps elements that are common to both sets.



'''