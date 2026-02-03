class Dog:
    def __init__(self, name):
        # Konstruktor – uruchamia się przy tworzeniu obiektu
        self.name = name
        print(f"Pies {self.name} został stworzony")

    def bark(self):
        # Zwykła metoda klasy
        print(f"{self.name}: Hau hau!")

    def __del__(self):
        # Destruktor – wywoływany przy usuwaniu obiektu
        print(f"Pies {self.name} został usunięty")


# Tworzenie obiektu
dog1 = Dog("Reksio")
dog1.bark()

# Usunięcie obiektu
del dog1
