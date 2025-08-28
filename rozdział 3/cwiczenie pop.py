# Napisz program, który:
#
# Tworzy listę ulubionych gier (np. 3 gry).
#
# Wypisuje całą listę.
#
# Usuwa ostatnią grę metodą .pop() i zapisuje ją do zmiennej.
#
# Wyświetla komunikat:
# Ostatnio usunięta gra to: <nazwa>
#
# Wypisuje listę po usunięciu.

#ctrl + / - zakomentowanie



gry = ['ets2', 'fortnite', 'forza']
print(gry)
top_gra = gry.pop(1)
print("Ulubiona gra to" ,top_gra )
print(gry)