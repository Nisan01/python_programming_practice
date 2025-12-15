

class Person:
    def __init__(self,age,height):
        self.ag=age
        self.hg=height
    def __str__(self):
     return f"The age is :{self.ag} and the height is : {self.hg}"
    
    def info(self):
            return print(f"The age is :{self.ag} and the height is : {self.hg}")


nishan=Person(15,20)
nishan.info()

class Person1:
    def __init__(self,age1,height1):
        self._ag=age1
        self._hg=height1
    @property
    def age(self):
        return self._ag  # return the age

    @property
    def height(self):
        return self._hg
      
    @age.setter
    def setAge(self,new_age):
        self._ag=new_age

        

roshan=Person1(20,45)
roshan_age=roshan.age 
print("Roshan's age is",roshan_age)   

roshan.setAge=60
print("Roshan's age is",roshan.age)   
