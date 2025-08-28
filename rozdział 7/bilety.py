active = True

koszyk = []

while active:
    wiek = input("Podaj wiek osoby lub wpisz 'koniec' aby podsumowac zakup")
    if wiek.lower() == 'koniec':
        active = False
    else:
        wiek = int(wiek)

    if wiek <= 3:
        cena = 0
        print("bilet darmowy")
    elif wiek <= 17:
        cena = 10
        print("bilet ulgowy 10zl")
    elif wiek <= 60:
        cena = 20
        print("bilet normalny 20zl")
    else:
        cena = 15
        print("bilet seniora 15zl")


    koszyk.append(cena)

suma = sum(koszyk)
print(suma)