# ----------------------------------------
# Zadanie 1 – klasy Student i School
# Tworzymy obiekty Student i dodajemy je do obiektu School
# ----------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        # Wyświetla informacje o uczniu
        print(self.name, self.age)


class School:
    def __init__(self, name):
        self.name = name
        self.students = []  # lista uczniów w szkole

    def addStudent(self, student):
        # Dodaje obiekt Student do listy uczniów
        self.students.append(student)

    def printStudents(self):
        # Wyświetla wszystkich uczniów w szkole
        print("Szkoła:", self.name)
        for student in self.students:
            print(student.name, student.age)


# --- Test ---
school = School("High School")
student1 = Student("John", 22)
school.addStudent(student1)
student2 = Student("Anna", 25)
school.addStudent(student2)
school.printStudents()



# ----------------------------------------
# Zadanie 2 – klasa Pizza
# Tworzymy pizzę, dodajemy składniki i wyświetlamy je
# ----------------------------------------

class Pizza:
    def __init__(self):
        self.ingredients = []  # lista składników pizzy

    def addIngredient(self, ingredient):
        # Dodaje składnik jeśli jest typu string
        if isinstance(ingredient, str):
            self.ingredients.append(ingredient)

    def showIngredients(self):
        # Wyświetla wszystkie składniki
        print("Składniki pizzy:")
        for ingredient in self.ingredients:
            print("-", ingredient)


# --- Test ---
pizza = Pizza()
pizza.addIngredient("ser")
pizza.addIngredient("szynka")
pizza.showIngredients()





# ----------------------------------------
# Zadanie 3 – klasa Employee
# Liczymy liczbę pracowników i zarządzamy listą obiektów
# ----------------------------------------

class Employee:
    numEmployees = 0        # liczba wszystkich pracowników (atrybut klasy)
    employeesList = []      # lista wszystkich obiektów Employee

    def __init__(self, name):
        self.name = name
        Employee.numEmployees += 1
        Employee.employeesList.append(self)

    def printEmployees(self):
        # Wyświetla wszystkich pracowników w liście
        print("Lista pracowników:")
        for employee in Employee.employeesList:
            print("-", employee.name)

    def removeEmployee(self, name):
        # Usuwa pracownika po imieniu z listy i zmniejsza licznik
        for employee in Employee.employeesList:
            if employee.name == name:
                Employee.numEmployees -= 1
                Employee.employeesList.remove(employee)
                break  # ważne, żeby nie iterować dalej po zmienionej liście


# --- Test ---
adam = Employee("Adam")
alex = Employee("Alex")
marian = Employee("Marian")

marian.printEmployees()
print("Liczba pracowników:", Employee.numEmployees)

adam.removeEmployee("Adam")
print("Liczba pracowników po usunięciu Adama:", Employee.numEmployees)
marian.printEmployees()





# ----------------------------------------
# Zadanie 4 – średni wiek uczniów w szkole
# Rozszerzenie Zadania 1
# ----------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print(self.name, self.age)


class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def addStudent(self, student):
        self.students.append(student)

    def printStudents(self):
        print("Szkoła:", self.name)
        for student in self.students:
            print(student.name, student.age)

    def averageAge(self):
        # Oblicza średni wiek wszystkich uczniów
        if not self.students:
            print("Brak uczniów w szkole")
            return

        total = 0
        for student in self.students:
            total += student.age

        avg = total / len(self.students)
        print("Średni wiek uczniów:", avg)


# --- Test ---
school = School("High School")
student1 = Student("John", 22)
school.addStudent(student1)
student2 = Student("Anna", 25)
school.addStudent(student2)

school.printStudents()
school.averageAge()
