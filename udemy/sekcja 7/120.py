# słowniki

# Tworzenie słownika
data = {'name': 'ola', 'age': 25}

# Odczyt wartości
print("Imię:", data['name'])

# Aktualizacja wartości
data['age'] = 22
print("Nowy wiek:", data['age'])

# Dodanie nowego klucza
city = 'warszawa'
data['city'] = city
print("Dodano miasto:", data)

# Usuwanie klucza
del data['city']
print("Po usunięciu miasta:", data)

# Długość słownika
print("Liczba elementów w data:", len(data))

# Czyszczenie słownika
data.clear()
print("Po wyczyszczeniu:", data)


# Tworzenie drugiego słownika
data2 = {'name': 'ola', 'age': 22, 'city': 'warszawa'}

# Kopiowanie słownika
copy = data2.copy()
print("Kopia słownika:", copy)

# fromkeys – tworzy nowy słownik z kluczami, wartości = None
print("Nowy słownik z fromkeys:", dict.fromkeys(('name', 'age', 'city')))

# get – bezpieczne pobieranie wartości
print("Kod pocztowy:", data2.get('postal code', 'default'))

# Sprawdzanie czy klucz istnieje
print("Czy 'name' jest w data2?", 'name' in data2)

# Klucze i wartości
print("Klucze:", data2.keys())
print("Wartości:", data2.values())

# Elementy (klucz, wartość) jako para
print("Elementy:", data2.items())
