
def getUserInformation(name,surname,job):
    name, surname = name.upper(), surname.upper()
    job = job.lower()
    name,surname,job = name.strip(), surname.strip(), job.strip()
    str = 'imie: ' + name + ' nazwisko: ' + surname + ' zawod: ' + job
    return str

user1 = getUserInformation("Ania", "Kowalska", "Programistka")
user2 = getUserInformation("Daniel", "Lis", "Administrator")

print(user1)
print(user2)