
while True:
    operacja = input("podaj znak (*,/,-,+,exit): ")
    if operacja == "exit":
        break

    num1 = int(input("podaj liczbe 1: "))
    num2 = int(input("podaj liczbe 2: "))

    if operacja == "+":
        wynik = num1 + num2
        print(wynik)
    elif operacja == "-":
        wynik = num1 - num2
        print(wynik)
    elif operacja == "*":
        wynik = num1 * num2
        print(wynik)
    elif operacja == "/":
        wynik = num1 / num2
        print(wynik)
    else:
        print("blad: nieznana operacja")
