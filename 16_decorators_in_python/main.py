
'''  
------------------Decorators---------------------

Decorators let you add extra behavior to a function, without changing the function's code.

A decorator is a function that takes another function as input and returns a new function.

 '''


def upperConverter(data):
    return(data.upper())


a=upperConverter("nisahan")
print(a)

def changecase(func):
    def wrapper():
        print(f"Calling {func.__name__}")
        return func().upper()
    return wrapper

@changecase
def myfunction():
    return "Nally"

@changecase
def another():
    return "Good Morning !!"

def greetingUser(f1, f2):
    return f1() + " " + f2()

print(myfunction())
print(another())
print(greetingUser(myfunction, another))



def myfunction1():
  return "Have a great day!"




print("----------New Line-----------------")



def decorate(x):
    def myFunction(*args,**kwargs):
      print("Good Morning !")
      
      print(x(*args,**kwargs))

      print("Bye")
    return myFunction  
''' 



 '''

@decorate
def printName():
    return"Hello World"

@decorate
def add(a,b):
    return(a+b)



printName()

add(10,5)