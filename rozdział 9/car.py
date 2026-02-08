class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def full_name(self):
        return f"{self.make} {self.model} {self.year}"

    def read_odometer(self):
        print(f"ten samochod ma przejechane {self.odometer_reading} km")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("nie mozna cofnąć przebiegu")

a3 = Car("Audi", "A3", 2020)
print(a3.full_name())
a3.read_odometer()
a3.odometer_reading = 200
a3.read_odometer()
a3.update_odometer(2000)
a3.read_odometer()
a3.update_odometer(1500)
a3.read_odometer()
