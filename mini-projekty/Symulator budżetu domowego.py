# Symulator budżetu domowego

transakcje = [

]


def dodaj_transakcje():
    print("dodaj transakcje")
    typ = input("podaj typ: ")
    kwota = float(input("podaj kwota: "))
    kategoria = input("podaj kategoria: ")
    transakcje.append({"typ": typ, "kwota": kwota, "kategoria": kategoria})
    print(f"dodano transakcje {typ} {kwota} {kategoria}")


def pokaz_saldo():
    print("saldo")

    suma_przychodow = 0
    suma_wydatkow = 0

    for transakcja in transakcje:
        if transakcja["typ"] == 'przychód':
            suma_przychodow += transakcja["kwota"]
        elif transakcja["typ"] == 'wydatek':
            suma_wydatkow += transakcja["kwota"]
    saldo = suma_przychodow - suma_wydatkow
    print(f"saldo: {saldo}")


def pokaz_historia():
    print("historia transakcji")
    for transakcja in transakcje:
        print(transakcja)


def podsumowanie_kategorii():
    wybor_kategorii = input("podaj kategorie do podsumowania: ")
    suma = 0
    for transakcja in transakcje:
        if transakcja["kategoria"] == wybor_kategorii:
            suma += transakcja["kwota"]
    print(f"suma dla kategorii:{wybor_kategorii} wynosi: {suma}")




def najwiekszy_wydatek():
    najwiekszy_wydatek = 0
    for transakcja in transakcje:
        if transakcja["typ"] == "wydatek":
            if transakcja["kwota"] > najwiekszy_wydatek:
                najwiekszy_wydatek = transakcja["kwota"]
    print(najwiekszy_wydatek)


while True:
    akcja = input("co chcesz zrobić (dodaj, saldo, historia, podsumowanie_kategorii, najwiekszy_wydatek, koniec): ) ")
    if akcja == "koniec":
        break

    elif akcja == "dodaj":
        dodaj_transakcje()
    elif akcja == "saldo":
        pokaz_saldo()
    elif akcja == "historia":
        pokaz_historia()
    elif akcja == "podsumowanie_kategorii":
        podsumowanie_kategorii()
    elif akcja == "najwiekszy_wydatek":
        najwiekszy_wydatek()
    else:
        print("nieznana operacja")