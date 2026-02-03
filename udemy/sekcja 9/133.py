import random


# ===== KLASA STUDENT =====
class Student:
    def __init__(self, name, surname, age, city):
        # Podstawowe dane studenta
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city

        # Dane, które mogą zostać ustawione później
        self.schoolName = None
        self.fieldOfStudy = None

    def print_info(self):
        # Wyświetla wszystkie informacje o studencie
        print(
            self.name,
            self.surname,
            self.age,
            self.city,
            self.schoolName,
            self.fieldOfStudy
        )


# ===== KLASA SCHOOL =====
class School:
    def __init__(self, name, city):
        # Podstawowe informacje o szkole
        self.name = name
        self.city = city

        # Lista studentów przypisanych do szkoły
        self.students = []

        # Dostępne kierunki nauki
        self.fields_of_study = ["IT", "Math"]

    def add_student(self, student):
        # Sprawdzamy, czy przekazany obiekt jest typu Student
        if isinstance(student, Student):
            self.students.append(student)

            # Przypisujemy studentowi nazwę szkoły
            student.schoolName = self.name

            # Losowo wybieramy kierunek studiów
            student.fieldOfStudy = random.choice(self.fields_of_study)

    def print_school_info(self):
        # Wyświetla informacje o szkole i jej studentach
        print("School name:", self.name, "| City:", self.city)
        for student in self.students:
            student.print_info()


# ===== TWORZENIE OBIEKTÓW =====

# Tworzymy pierwszego studenta
student1 = Student("John", "Smith", 21, "Math")
student1.schoolName = "Tech School"
student1.print_info()

# Dynamiczne dodanie nowego atrybutu do obiektu
student1.country = "USA"
print(student1.country)

# Drugi student
student2 = Student("James", "Smith", 21, "Math")

# Tworzymy szkołę
school = School("High School", "KRK")

# Dodajemy studentów do szkoły
school.add_student(student1)
school.print_school_info()

school.add_student(student2)
school.print_school_info()
