

class Animal:

    animalEar="rounded"

    def animalInfo(self):
        print(f"The animal name is {self.name} and its ear is {self.animalEar}")

    @classmethod
    def functionNormal(nick,changeNameEar):
        nick.animalEar=changeNameEar    


a =Animal()
a.name="cow"

a.animalInfo()

a.functionNormal("oval")
a.animalInfo()

print(Animal.animalEar)
