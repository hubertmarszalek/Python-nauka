employee = {
    "name": "<NAME>",
    "email": "<EMAIL>",
    "rank":"programmer",
    "salary":8000,
}

employee2 = {
    "name": "<NAME>",
    "email": "<EMAIL>",
    "rank":"manager",
    "salary":8000,
}

def promoteToManager(user):
    if user["rank"] == "manager":
        print("ta osoba jest menadzerem")
        return

    user["salary"] = user["salary"] * 1.50
    user["rank"] = "manager"
    return user

promoteToManager(employee)
print(employee)

promoteToManager(employee2)
print(employee2)