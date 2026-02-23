## 1. Fundamenty: Klasa, Atrybuty

# Klasa to szablon
class Pies:
    # __init__ to konstruktor - wywołuje się automatycznie przy tworzeniu obiektu
    def __init__(self, imie, rasa, wiek):
        self.imie = imie          # Atrybut instancji
        self.rasa = rasa
        self.wiek = wiek
        self.czy_glodny = True    # Atrybut może mieć wartość domyślną

    # Metoda - czyli co obiekt potrafi robić
    def szczekaj(self):
        print(f"{self.imie} mówi: Hau! Hau!")

    def nakarm(self):
        self.czy_glodny = False
        print(f"{self.imie} został nakarmiony.")

# Tworzenie obiektów (instancji klasy)
moj_pies = Pies("Reksio", "Kundelek", 5)
twoj_pies = Pies("Azor", "Owczarek", 3)

# Dostęp do danych i wywoływanie metod
print(f"Mój pies to {moj_pies.imie}, ma {moj_pies.wiek} lat.")
moj_pies.szczekaj()


## Dziedziczenie

class Zwierze:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def wydaj_dzwiek(self):
        pass # To jest metoda abstrakcyjna (do nadpisania)

class Kot(Zwierze):
    def wydaj_dzwiek(self):
        return "Miau!"

class Ptak(Zwierze):
    def __init__(self, nazwa, czy_lata=True):
        # super() wywołuje konstruktor klasy nadrzędnej (Zwierze)
        super().__init__(nazwa)
        self.czy_lata = czy_lata

    def wydaj_dzwiek(self):
        return "Ćwir!"

# Testowanie
pusiak = Kot("Mruczek")
tweety = Ptak("Tweety", czy_lata=True)

print(f"{pusiak.nazwa} robi: {pusiak.wydaj_dzwiek()}")
print(f"{tweety.nazwa} robi: {tweety.wydaj_dzwiek()}")

## Hermetyzacja

class KontoBankowe:
    def __init__(self, wlasciciel, saldo):
        self.wlasciciel = wlasciciel
        self.__saldo = saldo  # Podwójny podkreślnik sprawia, że atrybut jest "prywatny"

    def wplac(self, kwota):
        if kwota > 0:
            self.__saldo += kwota
            print(f"Wpłacono {kwota}. Aktualny stan: {self.__saldo}")

    def pokaz_saldo(self):
        return f"Stan konta dla {self.wlasciciel}: {self.__saldo} PLN"

konto = KontoBankowe("Jan Kowalski", 1000)
konto.wplac(500)
print(konto.pokaz_saldo())

# Próba: print(konto.__saldo) wyrzuci błąd! To chroni dane przed przypadkową zmianą.