zakupy = []
while True:
    akcja = input("Co chcesz zrobic: ")
    if akcja == "koniec":
        break

    elif akcja == "dodaj":
        produkt = input("Dodaj produkt: ")
        zakupy.append(produkt)
        print(f"Dodano {produkt}")

    elif akcja == "usuń".lower():
        usun = input("Co chcesz usunac")
        if usun in zakupy:
            zakupy.remove(usun)
            print(f"usunieto {usun}")
            break

    elif akcja == "wyświetl":
        for produkt in zakupy:
            print(produkt)
