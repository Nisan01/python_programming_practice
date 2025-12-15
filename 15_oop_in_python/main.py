'''

What is OOP?
OOP stands for Object-Oriented Programming.

Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

Advantages of OOP
Provides a clear structure to programs
Makes code easier to maintain, reuse, and debug
Helps keep your code DRY (Don't Repeat Yourself)
Allows you to build reusable applications with less code

The pass Statement
class definitions cannot be empty, 
but if you for some reason have a class definition with no content,
put in the pass statement to avoid getting an error.


'''


class fruit:
    a="Apple"


b=fruit()
c=fruit()
d=fruit()
print(b.a)
print(c.a)
print(d.a)



class PersonWater:
   def details(self,name,age):
      self.name=name
      self.age=age

      


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)



class Python:
  fullname="Nishan Chauhan"
  age=45


p11=Python()

print(p11.fullname)


class Python1:
  def __init__(self,fullname="Nishan kiran Chauhan",age=45):
     self.fullname=fullname
     self.age=age

  def name_age(self):
     print(f"{self.fullname} is {self.age} years old !!")   
     
  


p12=Python1()

print(p12)



