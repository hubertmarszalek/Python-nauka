# Przetwarzanie danych użytkowników
from functools import reduce

# Lista użytkowników
users = [
    {'name': 'Jan', 'age': 15},
    {'name': 'Anna', 'age': 25},
    {'name': 'Piotr', 'age': 30},
    {'name': 'Katarzyna', 'age': 22}
]

# 1. Filtrowanie – tylko pełnoletni (age >= 18)
users_filter = list(filter(lambda u: u['age'] >= 18, users))
print("Pełnoletni:", users_filter)

# 2. Mapowanie – pomnożenie wieku * 2
x2 = list(map(lambda u: u['age'] * 2, users_filter))
print("Wiek * 2:", x2)

# 3. Redukcja – suma wszystkich wartości z x2
age_sum = reduce(lambda x, y: x + y, x2)
print("Suma:", age_sum)
