from functools import reduce

# --- Prosta funkcja lambda do sumy dwóch liczb ---
sum_func = lambda x, y: x + y
print(sum_func(10, 3))

print("-------")

# --- Funkcja generująca funkcje (dobler/tripler) ---
def genFunc(n):
    return lambda x: x * n

dobler = genFunc(2)
print(dobler(10))  # 20

tripler = genFunc(3)
print(tripler(5))  # 15

print("------")

# --- Mapowanie funkcji lambda na listę (kwadraty) ---
listData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = map(lambda x: x ** 2, listData)
print(list(result))

# --- Mapowanie funkcji lambda na listę (mnożenie przez 3) ---
print(list(map(lambda x: x * 3, [1, 2, 3, 4, 5])))

print("------")

# --- Mapowanie zwykłej funkcji zamiast lambdy ---
def square(x):
    return x ** 2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = map(square, lista)
print(list(result))

print("------")

# --- Filtracja listy (imiona dłuższe niż 4 znaki) ---
names = ['adam', 'ola', 'wiktor', 'natalia']
result = filter(lambda x: len(x) > 4, names)
print(list(result))

print("------")

# --- Reduce: łączenie stringów ---
result = reduce(lambda x, y: x + " " + y, ("Ola", "Ania"))
print(result)

print("------")

# --- Reduce: iloczyn wszystkich elementów listy ---
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reduce(lambda x, y: x * y, numbers)
print(result)
