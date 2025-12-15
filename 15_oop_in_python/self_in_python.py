'''  
Without self, Python would not know which object's properties you want to access:

'''


class Car:
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year

    def car_info(self):
        print(f"Car is {self.name} model {self.model} made in {self.year}")    



p1=Car("Toyota","BGF001",1990)
p1.car_info()

p2=Car("Nishan","BGF001",1990)
p2.car_info()

p3=Car("Toyota","BGF001",1990)
p3.car_info()


class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)