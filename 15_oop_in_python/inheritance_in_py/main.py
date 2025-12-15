
'''

Inheritance in python
When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.

Python Inheritance Syntax
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class

'''


class Student:
    def __init__(self,name,semester,course):
        self.name=name
        self.sem=semester
        self.course=course

    def stdInfo(self):
        print(f"Name: {self.name}\nSemester: {self.sem}\nCourse: {self.course}")    


class AddedStudent(Student):
    def stdInfo1(self):
        print(f"New Std")   
    

s1=Student("Nishan",6,"BCA")
s1.stdInfo()

s2=AddedStudent("Roshan",4,"bca")
s2.stdInfo()

s2.stdInfo1()
