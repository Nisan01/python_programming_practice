'''
In react we write map , filter and reduce ....by 
const choices=[1,2,3,4]

{choices.map(index,item),(
))}
but in python we do this 

map(function,[List])
The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

'''
#An iterator generates elements on the fly, one at a time.

#Consumes less memory, especially for large datasets.

#this is actually not a list its an iterator so if we want to retrieve data more than once we can convert it into a list


def myfunc(a, b):
  return a + b

x =list(map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple')))

print(list(x))

print(" ".join(x))



def cube(x):
  return(x*x*x)

c=[4,5,6,8,9]

x1=map(cube,c)
print(list(x1))
