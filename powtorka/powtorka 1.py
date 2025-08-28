names = ['adam', 'marcel', 'eliza']
for name in names:
    print(name)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for number in numbers:
    print(number * 2)

wiek = input("Podaj wiek: ")
wiek = int(wiek)

if wiek >= 18:
    print("pelnoletni")
else:
    print("niepelnoletni")



numbers2 = [5, 12, 19, 3, 25]
for number in numbers2:
    if number > 10:
        print(number)


haslo = input("hasło: ")
haslo = str(haslo)
if haslo == "python123":
    print("zalogowano")
else:
    print("nie zalogowano")


ceny = {'jablko': 2, 'banan': 3, 'gruszka': 4}
for owoc, cena in ceny.items():
    print(f"{owoc} kosztuje {cena} zl")


users = {}

while True:
    imie = input("imie to: ")
    if imie == "stop":
        break
    if imie != "stop":
        wiek = input("podaj wiek: ")
        wiek = int(wiek)
        users[imie] = wiek

for imie, wiek in users.items():
    print(imie, wiek)



koszyk = {}

while True:
    produkt = input("produkt: ")
    if produkt == "koniec":
        break
    if produkt != "koniec":
        cena = input("cena: ")
        cena = int(cena)
        koszyk[produkt] = cena

for produkt, cena in koszyk.items():
    print(f"{produkt} kosztuje {cena} zl")

print(sum(koszyk.values()))





bilety = {}
cena = int(cena)
while True:
    wiek = input("podaj wiek: ")
    wiek = int(wiek)
    if wiek <= 3:

        cena = 0
        bilety[wiek] = cena
    if wiek <= 17:
        cena = 10
        bilety[wiek] = cena
    if wiek <= 60:
        cena = 20
        bilety[wiek] = cena
    if wiek > 60:
        cena = 15
        bilety[wiek] = cena
    if wiek == "koniec":
        break

print(sum(bilety.values()))