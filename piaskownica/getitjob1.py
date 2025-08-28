def czy_to_kobieta(imie):
    if imie.lower() == "kuba":   # najpierw wyjątek
        print("to mezczyzna")
    elif imie[-1] == "a":        # potem ogólna zasada
        print("to kobieta")
    else:
        print("to mezczyzna")

wynik = czy_to_kobieta("kuba")
print(wynik)

czy_to_kobieta(imie="adam")
czy_to_kobieta(imie="magda")
czy_to_kobieta(imie="marek")
czy_to_kobieta(imie="kuba")



def czy_to_kobieta1(imie):
    if imie.lower() == "kuba":   # najpierw wyjątek
        return False
    elif imie[-1] == "a":        # potem ogólna zasada
        return True
    else:
        return False



wynik = czy_to_kobieta1("kuba")
print(wynik)






def pralka(ubrania):
    czyste_ubrania = []
    for ubranie in ubrania:
        czyste_ubranie = ubranie.replace("brudne", "czyste")
        czyste_ubrania.append(czyste_ubranie)
    return czyste_ubrania



ubrania = ('brudne skarpetki', 'brudne spodnie')

wynik = pralka(ubrania)
print(wynik)





def czysc(ubranie):
    czyste_ubranie = ubranie.replace("brudne", "czyste")
    czyste_ubranie = czyste_ubranie.replace("brudna", "czysta")
    return czyste_ubranie

def pralka( *args, proszek):
    print(f"uzywam proszku {proszek}")
    czyste_ubrania = []
    for ubranie in args:
        czyste_ubrania.append(czysc(ubranie))
    return czyste_ubrania

brudne_ciuchy = [
    'brudne skarpetki',
    'brudne spodnie',
    'brudna koszulka',
]


wynik = pralka( *brudne_ciuchy, proszek='vizir')
print(wynik)





















