# Tworzenie krotek na różne sposoby
tuple1 = (1, 2, 3, 4) + (5,) + tuple([6, 7])
print("Typ obiektu:", type(tuple1))
print("Zawartość tuple1:", tuple1)

# Powielanie krotki
print("Powielanie krotki:", (1, 2) * 4)

# Sprawdzenie czy element istnieje w krotce
print("Czy 9 jest w tuple1?", 9 in tuple1)
print("Drugi element tuple1:", tuple1[1])
print("Długość tuple1:", len(tuple1))

# Minimum i maksimum
print("Minimalna wartość:", min(tuple1))
print("Maksymalna wartość:", max(tuple1))

# Konwersja listy na krotkę i krotki na listę
lista = [10, 20, 30]
tuple2 = tuple(lista)
print("Lista jako krotka:", tuple2)

lista2 = list(tuple1)
print("Krotka jako lista:", lista2)

# Rozpakowywanie krotki
a, b, c = (100, 200, 300)
print("Rozpakowane wartości:", a, b, c)

# Zagnieżdżone krotki
tuple3 = (1, (2, 3), (4, 5, 6))
print("Zagnieżdżona krotka:", tuple3)
print("Dostęp do elementu w środku:", tuple3[1][1])

# Count i index
tuple4 = (1, 2, 2, 3, 2, 4)
print("Ile razy 2 występuje:", tuple4.count(2))
print("Pierwszy index 2:", tuple4.index(2))
