class Car:
    def __init__(self, brand, model, year):
        self.carName = brand + " " + model
        self.productionDate = year

    def printInfo(self):
        print(self.carName + " " + str(self.productionDate))


mustang = Car("For", "Mustang", 2000)
mustang.printInfo()

a3 = Car("Audi", "A3", 2000)
a3.printInfo()



class Car2:
    def __init__(self, brand, name,color, year):
        self.brand = brand
        self.name = name
        self.color = color
        self.year = year
        self.mileage = 1
        self.printInfo()

        print("Wywolanie konstruktora", self.brand, self.name, self.color)

    def printInfo(self):
        print(f"{self.brand}  {self.name} {self.color} {self.year} {self.mileage} mi")

mustang = Car2('Ford', 'Mustang', "yelow", 2000)
mustang.mileage = 100
mustang.topSpeed = 230
mustang.printInfo()
print(mustang.topSpeed)
print(mustang.printInfo())
