# Definicja klasy Samochod
class Samochod:
    def __init__(self, marka, kolor):
        # Atrybuty samochodu
        self.marka = marka
        self.kolor = kolor
        self.predkosc = 0       # aktualna prędkość
        self.dystans = 0        # łączny dystans przejechany w km

    def przyspiesz(self, ile):
        self.predkosc += ile
        print(f"{self.marka} przyspieszył o {ile} km/h")
        print(f"Aktualna prędkość: {self.predkosc} km/h")

    def zwolnij(self, ile):
        self.predkosc -= ile
        if self.predkosc < 0:
            self.predkosc = 0
        print(f"{self.marka} zwolnił o {ile} km/h")
        print(f"Aktualna prędkość: {self.predkosc} km/h")

    def zatrzymaj(self):
        self.predkosc = 0
        print(f"{self.marka} zatrzymał się")
        print(f"Aktualna prędkość: {self.predkosc} km/h")

    def jedz(self, godziny):
        if self.predkosc == 0:
            print(f"{self.marka} stoi, nie przejechał żadnych kilometrów.")
            return
        przejechano = self.predkosc * godziny
        self.dystans += przejechano
        print(f"{self.marka} przejechał {przejechano} km w tej jeździe")
        print(f"Łączny dystans: {self.dystans} km")

    def aktualna_predkosc(self):
        print(f"{self.marka} jedzie z prędkością {self.predkosc} km/h")

    def raport(self):
        print(f"Samochód: {self.marka}, kolor: {self.kolor}")
        print(f"Aktualna prędkość: {self.predkosc} km/h")
        print(f"Łączny dystans: {self.dystans} km")


# ---------------------------
# TEST: Tworzenie obiektu i jazda
# ---------------------------
ford = Samochod("Ford", "czerwony")

# Przyspieszanie i jazda
ford.przyspiesz(50)
ford.jedz(2)      # 50 km/h * 2 h = 100 km

ford.przyspiesz(30)
ford.jedz(1.5)    # 80 km/h * 1.5 h = 120 km

# Zwalnianie i jazda
ford.zwolnij(70)
ford.jedz(0.5)    # 10 km/h * 0.5 h = 5 km

# Zatrzymanie samochodu
ford.zatrzymaj()

# Raport końcowy
ford.raport()
