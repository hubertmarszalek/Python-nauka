#program 1
imiona = ['jakub', 'ania', 'filip', 'natalia', 'marek', 'natan']

litera = input("podaj litere na kt rozpoczyna sie imie")
for imie in imiona:
    if imie.startswith(litera):
        print(imie)


#program 2
zakupy = []

while True:
    zakup = input("Co chcesz kupic? ")
    if zakup == "koniec":
        for z in zakupy:
            print(z)
        break
    elif zakup != "koniec":
        zakupy.append(zakup)
        print(f"Dodano {zakup}")


#program 3
produkty = []
while True:
    produkt = input("Czy chcesz cos kupic? ")
    if produkt == "nie":
        for p,c in produkty:
            print(p, c)
        break

    elif produkt == "tak":
        nazwa = input("Nazwa produktu? ")
        cena = input("Cena produktu? ")
        cena = int(cena)
        produkty.append((nazwa, cena))

suma = sum(cena for nazwa, cena in produkty)
print(suma)



#program 4
uzytkownicy = []
while True:
    uzytkownik = input("wpisz stop jezeli chcesz zakonczyc lub kliknij enter")
    if uzytkownik == "stop":
        for i, w in uzytkownicy:
            print(f"imie: {i} - wiek: {w}")
        break

    elif uzytkownik != "stop":
        imie = input("Imie? ")
        wiek = input("Wiek? ")
        wiek = int(wiek)
        uzytkownicy.append((imie, wiek))



#program 5
products = []

while True:
    akcja = input("Co chcesz zrobic? (dodaj, usun, wuswietl, koniec)")
    if akcja == "koniec":
        break

    elif akcja == "dodaj":
        product = input("dodaj produkt ")
        products.append(product)
        print(f"dodano {product}")
    elif akcja == "usun":
        usun = input("co usuwasz ")
        products.remove(usun)
        print(f"usunieto {usun}")

    elif akcja == "wyswietl":
        for product in products:
            print(product)


#program 6
liczby = []
while True:
    liczby1 = input("stop lub enter ")
    if liczby1 == "stop":
        for liczba in liczby:
            if liczba % 2 == 0:
                print(liczba)

        break

    elif liczby1 != "stop":
        liczba = input("podaj liczbe ")
        liczba = int(liczba)
        liczby.append(liczba)



