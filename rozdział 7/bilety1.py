bilety = {}

while True:
    wiek = input("podaj wiek: ")
    if wiek.lower() == "koniec":
        break
    wiek = int(wiek)
    if wiek <= 3:
        cena = 0
    elif wiek <= 17:
        cena = 10
    elif wiek <= 60:
        cena = 20
    else:
        cena = 30
    bilety[wiek] = cena


print(sum(bilety.values()))

zadania = []

while True:
    print("\nCo chcesz zrobić? (dodaj / usuń / pokaż / koniec)")
    akcja = input("Wpisz akcję: ").lower()

    if akcja == "dodaj":
        nowe_zadanie = input("Podaj nowe zadanie: ")
        zadania.append(nowe_zadanie)
        print(f"Dodano zadanie: {nowe_zadanie}")

    elif akcja == "usuń":
        if not zadania:
            print("Brak zadań do usunięcia.")
            continue
        print("Aktualne zadania:")
        for i, zadanie in enumerate(zadania, start=1):
            print(f"{i}. {zadanie}")
        numer = input("Podaj numer zadania do usunięcia: ")
        if numer.isdigit():
            numer = int(numer)
            if 1 <= numer <= len(zadania):
                usuniete = zadania.pop(numer - 1)
                print(f"Usunięto zadanie: {usuniete}")
            else:
                print("Niepoprawny numer zadania.")
        else:
            print("Podaj poprawny numer.")

    elif akcja == "pokaż":
        if not zadania:
            print("Brak zadań do wyświetlenia.")
        else:
            print("Twoje zadania:")
            for i, zadanie in enumerate(zadania, start=1):
                print(f"{i}. {zadanie}")

    elif akcja == "koniec":
        print("Koniec działania programu.")
        break

    else:
        print("Nieznana akcja, spróbuj ponownie.")
