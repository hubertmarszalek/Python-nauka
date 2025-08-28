zadania = []

while True:
    akcja= input("Co chcesz zrobić z zadaniami (dodaj, usun, wyswietl, koniec)")
    if akcja == "koniec":
        break

    elif akcja == "dodaj":
       nazwa = input("Jaka nazwa zadania?: ")
       priorytet = input("Jaki priorytet zadania?: ")
       zadanie = {"nazwa": nazwa, "priorytet": priorytet}
       zadania.append(zadanie)
       print(f"Pomyślnie dodano zadanie: {nazwa} które ma  {priorytet} priorytet")

    elif akcja == "usuń":
        usun = input("Jakie zad chcesz usunac?: ")
        znaleziono = False
        for item in zadania:
            if item["nazwa"] == usun:
                zadania.remove(item)
                print(f"Usunieto zadanie {usun}")
                znaleziono = True
                break

        if not znaleziono:
            print("Błedna nazwa")

    elif akcja == "wyświetl":
        if not zadania:
            print("Brak zadań")
        else:
            for zadanie in zadania:
                print(f"{zadanie['nazwa']} - {zadanie['priorytet']}")
