age = 65
if age < 2:
    print("niemowle")
elif age > 2 and age < 4:
    print("male dziecko")
elif age > 4 and age < 13:
    print("dziecko")
elif age > 13 and age < 20:
    print("nastolatek")
elif age > 20 and age < 65:
    print("dorosly")
else:
    print("senior")


favourite_fruit = ["apple", "banana", "orange"]
if 'banana' in favourite_fruit:
    print("you very likes banana")
if 'ananas' in favourite_fruit:
    print("you very likes ananas")