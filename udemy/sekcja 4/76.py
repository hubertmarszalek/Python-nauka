numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number > 8:
        break

    if number % 2 == 0:
        continue
    print(number**2)

else:
    print("koniec")