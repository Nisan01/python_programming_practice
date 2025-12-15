

#parameterized constructor

class Animal:
    def __init__(self,name,type):
     self.name=name
     self.type=type



a=Animal("cow","domestic")
a.name="cow"
print(a.name)


#default constructor

class Book:
   def __init__(self):
      print("this is a default constructor")

a1=Book()      