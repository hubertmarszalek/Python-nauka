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

a3 = Car("Audi", "A3", 2020)
print(a3.full_name())
a3.read_odometer()
a3.odometer_reading = 200
a3.read_odometer()