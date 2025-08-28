# Pracownicy w liście z zwiększoną pensją

employees = []

def addEmplloyee(email, salary):
    e = {
        "email": email,
        "salary": salary,
    }
    employees.append(e)


addEmplloyee("<EMAIL>", 6000)
addEmplloyee("<EMAIL>", 8000)
addEmplloyee("<EMAIL>", 10000)

def increaseSalary(employees, pctIncrease):
    for employee in employees:
        employee["salary"] += employee["salary"] * pctIncrease
    print(employees)

increaseSalary(employees, 0.2)
