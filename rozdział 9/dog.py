class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"Dog {self.name} sit")

    def roll_over(self):
        print(f"Dog {self.name} roll over")

dog1 = Dog("reksio", 5)
dog1.sit()
dog1.roll_over()