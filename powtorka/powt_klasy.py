class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print(self.name, self.age)


st1 = Student("John", 22)
st1.printInfo()



class School:
    students = []
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def addStudent(self,name, age):
        self.name = name
        self.age = age


    def printStudents(self):
        for student in self.students:
            print(student.name, student.age)

student1 = Student("John", 22)

