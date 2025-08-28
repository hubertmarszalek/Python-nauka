dog_age = int(input("dog age: "))
if dog_age == 1:
    human_age = dog_age *15
elif dog_age == 2:
    human_age = 15 + (dog_age - 1) * 9
elif dog_age > 2:
    human_age = 24 + (dog_age - 2) * 5
else:
    human_age = 0
    print("blad")

print(human_age)