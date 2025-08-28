def calculateHumanYears(dog_age):
    if dog_age == 1:
        human_age = dog_age *10.5
        return human_age
    elif dog_age == 2:
        human_age = dog_age *10.5
        return human_age
    else:
        human_age = 21 + (dog_age - 2) * 4
        return human_age

while True:

    func_dog_age = int(input("wprowadz wiek psa aby przeliczyc na ludzki: "))
    x = calculateHumanYears(func_dog_age)
    print(f"{func_dog_age} to {x} lat na lata ludzkie")
    if func_dog_age == 0:
        break