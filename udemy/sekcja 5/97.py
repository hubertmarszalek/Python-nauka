def createUserProfile(firstName,lastName,age,city):
    user = {
        "firstName": firstName,
        "lastName": lastName,
        "age": age,
        "city": city,
    }
    return user

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

user1 = createUserProfile(firstName, lastName, age, city)

print(f"User profile created!\nName: {user1['firstName']} {user1['lastName']}\nAge: {user1['age']}\nCity: {user1['city']}")
