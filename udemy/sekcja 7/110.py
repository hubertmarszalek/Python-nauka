# Praca na łańcuchach znaków
string = 'hello'


print(string[1])           # -> 'e' (indeksowanie zaczyna się od 0)
print(string[2:4])         # -> 'll' (wycinek od indeksu 2 do 3)

# Sprawdzanie obecności znaku/ciągu
print('o' in string)       # -> True
print('o' not in string)   # -> False

# Modyfikacje i sprawdzanie
print("hej".capitalize())               # -> 'Hej' (pierwsza litera wielka)
print('ok ok ok'.count('ok'))           # -> 3 (ile razy występuje 'ok')

print('test'.center(10, '-'))           # -> '--test---' (wyśrodkowanie)

print("hello world".endswith('world'))  # -> True
print("hello world".startswith('hello'))# -> True

# Szukanie fragmentów
print("ala ma kota".find("ma"))         # -> 4 (indeks pierwszego wystąpienia)
print("ala ma kota".find("test"))       # -> -1 (brak w stringu)

print("ala ma kota i ma psa".rfind("ma"))  # -> 14 (ostatnie wystąpienie)

# Usuwanie białych znaków
print('\n \t  test '.lstrip())          # usuwa z lewej
print(' test \n \t'.rstrip())           # usuwa z prawej
print('\n \t test \t \n'.strip())       # usuwa z obu stron

# Zamiana tekstu
print('hejka'.replace('hejka', 'hej'))  # -> 'hej'

# Sprawdzanie typu zawartości
print('123456'.isalnum())   # True (same cyfry/litery)
print('1234'.isalpha())     # False (bo cyfry)
print('test'.isalpha())     # True (same litery)
print('test'.isalnum())     # True (litery też się liczą)

print('test'.islower())     # True
print('test'.isupper())     # False
print('test'.isspace())     # False (nie same spacje)

# Sklejanie elementów listy
print('-'.join(['ania', 'ola', 'rafal']))  # -> 'ania-ola-rafal'

# Długość łańcucha
print(len('hello world'))   # -> 11
