class Pies:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def szczekaj(self):
        print(f"{self.imie} mowi hau hau ")

    def starzej_sie(self):
        self.wiek += 1
        print(f"{self.imie} ma teraz {self.wiek} lat")

reksio = Pies("Reksio", 3)
reksio.starzej_sie()
reksio.szczekaj()


class Samochod:
    def __init__(self, marka, kolor):
        self.marka = marka
        self.kolor = kolor
        self.predkosc = 0

    def przyspiesz(self, ile):
        self.predkosc += ile
        print(f"{self.marka} przyspieszyl o {ile}")


    def zwolnij(self, ile2):
        if ile2 > self.predkosc:
            self.predkosc = 0

        self.predkosc = self.predkosc - ile2
        print(f"{self.marka} zwolnil o {ile2}")

    def zatrzymaj(self):
        self.predkosc = 0
        print("samochod zatrzymal sie ")

    def aktualna_predkosc(self):
        print(f"{self.marka} jedzie z prekoscia {self.predkosc}")


ford = Samochod("ford", "czerwony")
ford.przyspiesz(50)
ford.przyspiesz(100)
ford.zwolnij(70)
ford.aktualna_predkosc()
ford.zatrzymaj()