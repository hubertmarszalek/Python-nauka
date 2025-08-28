from os import remove

produkty = []
while True:
    produkt = input("Wpisz produkty: ")
    if produkt == "koniec":
        break
    elif produkt == "usuń":
        usun = input("Co usuwasz: ")
        for produkt, cena in produkty:
            if produkt == usun:
                produkty.remove((produkt, cena))
                print(f"usunieto {produkt}")
                break
    elif produkt != "koniec":
        cena = input("Wpisz cena: ")
        cena = int(cena)
        produkty.append((produkt, cena))


for produkt, cena in produkty:
    print(f"{produkt} kosztuje {cena} zl")