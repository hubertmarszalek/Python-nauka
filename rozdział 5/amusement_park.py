age = 30
if age < 4:
    print("Bilet bezplatny")
elif age < 18:
    print("Bielt 25 zl")
else:
    print("Bielt 40 zl")



age = 5
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Twoj bilet kosztuje {price}")