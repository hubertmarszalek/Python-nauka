# 1. Tworzymy pustą listę, w której będą przechowywane książki
ksiazki = []

while True:  # Pętla działa dopóki nie wpiszesz "koniec"
    # 2. Pytamy użytkownika, co chce zrobić
    akcja = input("Co chcesz zrobić? (dodaj, usuń, wyświetl, koniec): ").lower()

    # 3. Kończymy program
    if akcja == "koniec":
        break

    # 4. Dodawanie książki
    elif akcja == "dodaj":
        tytul = input("Podaj tytuł książki: ")
        autor = input("Podaj autora książki: ")

        # Tworzymy słownik z danymi książki
        ksiazka = {"tytul": tytul, "autor": autor}

        # Dodajemy słownik do listy
        ksiazki.append(ksiazka)

        print(f"Dodano książkę: {tytul} - {autor}")

    # 5. Usuwanie książki po tytule
    elif akcja == "usuń":
        usun = input("Podaj tytuł książki do usunięcia: ")
        znaleziono = False

        # Szukamy książki w liście
        for item in ksiazki:
            if item["tytul"].lower() == usun.lower():
                ksiazki.remove(item)
                print(f"Usunięto książkę: {usun}")
                znaleziono = True
                break  # przerywamy pętlę po usunięciu

        if not znaleziono:
            print("Nie znaleziono takiej książki.")

    # 6. Wyświetlanie listy książek
    elif akcja == "wyświetl":
        if not ksiazki:
            print("Lista książek jest pusta.")
        else:
            print("\nTwoje książki:")
            for i, item in enumerate(ksiazki, start=1):
                print(f"{i}. {item['tytul']} - {item['autor']}")
            print()  # pusty wiersz dla czytelności

    # 7. Obsługa nieznanej komendy
    else:
        print("Nieznana komenda. Wpisz: dodaj, usuń, wyświetl lub koniec.")
