class Employee:
    numEmployees = 0
    employeesList = []

    def __init__(self, name):
        self.name = name
        Employee.numEmployees += 1
        print(self.name, "numEmployees:", Employee.numEmployees)

        Employee.employeesList.append(self)

    def printEmployees(self):
        for employee in Employee.employeesList:
            print(employee.name)

employee1 = Employee("John")
employee2 = Employee("Jane")
employee3 = Employee("Doe")
employee4 = Employee("Doe")
employee5 = Employee("Doe")
print(Employee.numEmployees)

employee1.printEmployees()