#list has following methods like append(),sort(),sort(reverse=true),reverse,index() gives the index value

list=[1,40,8,92,9,22,45]

list.append(12)
list.sort()

print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(f"reversed list{list}")


list.index(8)
print(list.index(8))

#counting number of time something is repeated 

a=[2,5,8,9,2,4,5,2,6,2,6]

print(a.count(2))

#whenever we copy list to another variable without using copy method this is going to create or point out to 
#same reference thats why change in another variable also changes the intital variable

m=a
m[1]=12
print("Original value of a ",a)
print(m)

#so we use copy()method this actually creates the copy of the list 

m=a.copy()
m[1]=22
print(a)
print(m,"here is change")

#remove(x),it removes the first occurence in the list
#insert(1,55),it adds or insert the value 55 at index 1

print(list)
list.insert(1,55)

print(list)


list2=[200,500]

list.extend(list2)
print(list)

#using concatination

print(list+list2,"after concatination")