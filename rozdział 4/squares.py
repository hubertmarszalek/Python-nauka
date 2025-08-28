from string import digits

squares = []  # Tworzymy pustą listę, która będzie przechowywać liczby będące kwadratami

for value in range(1, 11):  # Pętla for przechodzi przez liczby od 1 do 10 (11 nie jest wliczane)
    square = value ** 2     # Dla każdej liczby obliczamy jej kwadrat (czyli liczba * liczba)
    squares.append(square)  # Dodajemy wynik (kwadrat) do listy squares

print(squares)  # Po zakończeniu pętli wypisujemy całą listę kwadratów

print(digits)  # wypisuje liczby wszytskie
print(min(digits))   #wypisuje najmniejsza
print(max(digits))   #wypisuje najw.










































