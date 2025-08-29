from random import randint

i = randint(1,100)
proby = 0

print("Zgadnij liczbę od 1 do 100")

while True:

    odp = int(input("podaj liczbe: "))
    proby += 1

    if odp == i:
        print(f"zgadłeś za {proby} razem, liczba to: {i}")
        break
    elif odp > i:
        print(f"za dużo")
    elif odp < i:
        print("za mało")