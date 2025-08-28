height = input("ile masz wzrostu")
height = int(height)
if height > 100:
    print("Mozesz wejsc")
else:
    print("Nie mozesz wejsc")




number = input("podaj liczbe a powiem ci czy jest parzysta czy nie")
number = int(number)
if number % 2 == 0:
    print("jest parzysta")
else:
    print(f"{number} jest nie parzysta")



auto = input("jaki samochod chcesz wypozyczyc")
print(f"sprawdze czy {auto} jest dostepne")


stolik = input("Witamy, na ile osob potrzebujecie stolik? ")
stolik = int(stolik)
if stolik > 8:
    print("prosze zaczekac")
else:
    print(f"stolik na {stolik} osób gotowy")


liczba = input("podaj liczbe: ")
liczba = int(liczba)

if liczba % 10 == 0:
    print(f"liczba {liczba} jest wielokrotnoscia 10")
else:
    print("nie jest")