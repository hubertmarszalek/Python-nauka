numbers=[]


while True:
    number = (input("podaj liczby aby obliczyc srednia lub exit jak skonczysz: "))
    if number == 'exit':
        break
    else:
        print("blad")
    number = float(number)
    numbers.append(number)
    print(f"dodales {number}")



srednia = sum(numbers)/len(numbers)
print(f'srednia to {srednia:.2f}')