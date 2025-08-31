import math
import random

# --- Funkcje wbudowane ---

# Wartość bezwzględna
print("abs:", abs(4))
print("abs:", abs(-4))

# Największa i najmniejsza liczba
print("max:", max(1, 5, -3, 23, 2, 33))
print("min:", min(1, 5, -3, 23, 2, 33))

# Potęgowanie
print("pow:", pow(4, 3))   # 4 ** 3 = 64

# --- Moduł math ---

# Pierwiastek kwadratowy
print("sqrt:", math.sqrt(100))  # 10.0

# Zaokrąglanie
print("round:", round(12.3454))        # 12
print("round(3):", round(12.3454, 3))  # 12.345

# --- Moduł random ---

# Losowy float od 0 do 1
print("random:", random.random())

# Losowy element z listy / krotki
print("choice (lista):", random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print("choice (krotka):", random.choice(("ola", "amelia", "miau")))

# Losowa liczba z podanego zakresu (start, stop, krok)
print("randrange:", random.randrange(1, 20, 5))  # np. 1, 6, 11, 16

# Losowa liczba całkowita (od a do b, włącznie)
print("randint:", random.randint(1, 10))

# lotto
print("sample:", random.sample(range(1, 50), 6))  # np. losowanie '6 z 49'
