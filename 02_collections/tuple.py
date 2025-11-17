
#tuple are unchangeable or immutable and ordered collections defined using () brackets


a=(1,5,6,8)
print(a)

print(type(a))
#if there is ony one item then , comma should be placed after the element
c=(1,)
print(c)

#if i want to change the tuple i can convert this to change
print(a)
b=list(a)
b.append(5)
c=tuple(b)
print(c)

#indexing in tuple

print(c[0])
print(c[0:],"c 0:")
print(c[1:])
print(c[2:4])
print(c[:-2])

if 5 in c:
    print("5 is present")
else:
    print("not present")    


animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8])
print(animals[1:8:3])


#tuple method like index()
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)