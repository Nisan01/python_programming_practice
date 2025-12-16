
'''  Class variables are defined at the class level and are shared among all instances of the class. 
They are defined outside of any method and are usually used to store 
information that is common to all instances of the class. For example,
 a class variable can be used to store the number of instances of a class that have been created. '''

class Car:
    
    companyName="Nishan"
    classVariable=0

    def __init__(self,name):
        self.n=name
        Car.classVariable+=1


    def showName(self):
        print(f"The name of the Car is {self.n} ,it belongs to {self.companyName} and is {self.classVariable}")    




s1=Car("Toyota")
s1.companyName="TWD"
s1.showName()    


s2=Car("Merchedes")
s2.showName()        

