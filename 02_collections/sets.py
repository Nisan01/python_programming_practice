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
common=d & e


common1="".join(sorted(common))
print(common1)

