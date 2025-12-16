
''' A class method is a type of method that is bound to the class and not the instance of the class. 
In other words, it operates on the class as a whole, rather than on a specific instance of the class
. Class methods are defined using the "@classmethod" decorator, followed by a function definition. 
The first argument of the function is always "cls," which represents the class itself. '''


class Person:
    def __init__(self,name,age):
        self.n1=name
        self.ag=age
    
    @classmethod
    def stringFormatter(cls,providedName):
        return cls(providedName.split(",")[0],int(providedName.split(",")[1]))


print(" ")
p1=Person("Nishan",15)
print(p1.n1)
print(p1.ag)

providedName="Roshan,13"

pp1=Person.stringFormatter(providedName)
print(pp1.n1)
print(pp1.ag)