data = ["apple", "banana", "", "cherry", "date"]
for fruit in data:
    if not fruit:
        continue  # Pomiń puste ciągi
    print(fruit.capitalize())


scores = [92, 85, 99, 78, 82, 100, 67, 88]
for score in scores:
    if score < 80:
        continue # Pomiń niskie wyniki

    print("Gratulacje, twój wynik: ", score)


#.2f ogranicza do 2 miejsc po przecinku
output = "Dane: {0:.2f} i {1:.2f}".format(3.1415926, 2.71828)
print(output)

n = 5
while n > 0:
    print(n)
    n -= 1
else:
    print('Pętla zakończyła się normalnie.')


n = 10
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} * {j} = {i * j}", end='\t')
    print()  # Przejście do nowej linii dla następnego mnożnika





"""
print("Ile km przejedziesz")

cena_paliwa = float(input("Podaj cene paliwa: "))
koszt_paliwa = float(input("Ile zapłaciłes na stacji: "))
spalanie = float(input("Podaj spalanie"))
dystans = (koszt_paliwa/cena_paliwa) * (100/spalanie)
print(f"dystans = {dystans:.2f} km")
"""


kfc = []
pyszne = []

while True:
    akcja = input("Wybierz miejsce pracy (kfc/pyszne/koniec/podsumuj): ").lower()

    if akcja == "koniec":
       break


    if akcja.lower() == "kfc":
        godziny_kfc = float(input("Podaj godziny kfc: "))
        kfc.append(godziny_kfc)
        stawka_kfc = float(input("Podaj stawka kfc: "))
        kfc.append(stawka_kfc)
        zarobek_kfc = godziny_kfc * stawka_kfc

    if akcja.lower() == "pyszne":
        godziny_pyszne = float(input("Podaj godziny pyszne: "))
        pyszne.append(godziny_pyszne)
        stawka_pyszne = float(input("Podaj stawka pyszne: "))
        pyszne.append(stawka_pyszne)
        zarobek_pyszne = godziny_pyszne * stawka_pyszne

    if akcja.lower() == "podsumuj":
        akcja_podsumowanie = input("kfc, pyszne czy razem?")
        if akcja_podsumowanie == "kfc":
            print(f"Zarobek w kfc to: {zarobek_kfc}")
        if akcja_podsumowanie == "pyszne":
            print(f"Zarobek w pyszne to: {zarobek_pyszne}")
        if akcja_podsumowanie == "razem":
            razem = zarobek_kfc + zarobek_pyszne
            print(f"Zarobek razem to: {razem}")






print("---Stacja benzynowa---")

ceny_paliw = {
    "pb98": 6.45,
    "pb95": 6.10,
    "on": 5.85,
    "lpg": 2.75
}

while True:
    wybor = input("Co tankujesz: (Pb98/Pb95/ON/LPG)")


    if wybor.lower() == "pb98":
        licznik_pb98 = float(input("Ile litrow zatankowwałes"))
        suma_pb98 = licznik_pb98 * ceny_paliw["pb98"]
        #liczenie zasiegu
        spalanie = float(input("Podaj spalanie: "))
        dystans = (suma_pb98/ceny_paliw["pb98"]) * (100/spalanie)

        print(f"Za Pb98 płacisz: {suma_pb98} zł")
        print(f"Max zasieg to: {dystans:.2f} km")


    if wybor.lower() == "pb95":
        licznik_pb95 = float(input("Ile litrow zatankowwałes"))
        suma_pb95 = licznik_pb95 * ceny_paliw["pb95"]
        #liczenie zasiegu
        spalanie = float(input("Podaj spalanie: "))
        dystans = (suma_pb95 / ceny_paliw["pb95"]) * (100 / spalanie)

        print(f"Za Pb98 płacisz: {suma_pb95} zł")
        print(f"Max zasieg to: {dystans:.2f} km")

    if wybor == "on":
        licznik_on = float(input("Ile litrów zatankowałeś: "))
        suma_on = licznik_on * ceny_paliw["on"]

        spalanie = float(input("Podaj spalanie: "))
        dystans = (licznik_on * 100) / spalanie

        print(f"Za ON płacisz: {suma_on:.2f} zł")
        print(f"Max zasięg to: {dystans:.2f} km")

    if wybor == "lpg":
        licznik_lpg = float(input("Ile litrów zatankowałeś: "))
        suma_lpg = licznik_lpg * ceny_paliw["lpg"]

        spalanie = float(input("Podaj spalanie: "))
        dystans = (licznik_lpg * 100) / spalanie

        print(f"Za LPG płacisz: {suma_lpg:.2f} zł")
        print(f"Max zasięg to: {dystans:.2f} km")
