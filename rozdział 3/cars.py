cars = ['bmw', 'maseratti', 'audi']
cars.sort()  #sortowanie alfabetyczne
print(cars)

cars.sort(reverse=True)   #sort. odwrotna kolejnosc
print(cars)


cars = ['bmw', 'maseratti', 'audi']
print("Oto lista pocz:")
print(cars)
print(sorted(cars))    # chwilowe (nie stałe) sortowanie listy
print(cars)
print(sorted(cars, reverse=True)) #chwilowe (nie stałe) sortowanie listy ale na odwrót

#odwrócenie kolejnosci bez sortowania
cars.reverse()
print(cars)
len(cars)