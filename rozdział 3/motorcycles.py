
#zamiana w liście
motorcycles = ['honda', 'honda', 'suzuki', 'yamaha']
print(motorcycles)
motorcycles[1] = 'bmw'
print(motorcycles)


#dodawanie do listy
motorcycles_01 = ['honda', 'suzuki', 'yamaha']
motorcycles_01.append('bmw')
print(motorcycles_01)


#tw listy
cars = []
cars.append('honda')
cars.append('bmw')
cars.append('audi')
print(cars)

#dodawanie kilku rzeczy na raz
cars.extend(['honda', 'suzuki', 'yamaha'])


#wstawianie nowego elementu na dana pozycje
cars_01 = ['honda', 'suzuki', 'bmw', 'audi', 'dacia', 'ford']
cars_01.insert(2, 'mercedes')
print(cars_01)

#usunięcie elementu wg liczby
del cars_01[0]
print(cars_01)

#metoda pop - usuwa ale zachowuje w pamięci
motorcycles_02 = ['honda', 'suzuki', 'bmw', 'audi']
print(motorcycles_02)

popped_motorcycles = motorcycles_02.pop()
print(motorcycles_02)
print(popped_motorcycles)

cars_01 = ['honda', 'suzuki', 'bmw', 'audi']

last_owned = cars_01.pop() #usuwa od tyłu
print(f"Ostatnio zakupione przeze mnie auto to {last_owned.title()}")

#usuniecie z dowolnego miejsca
cars_01=['honda', 'suzuki', 'bmw', 'audi']
first_owned = cars_01.pop(0) #wskazanie na miejsce
print(first_owned)


#usuniecie przez nazwe
truck = ['scania', 'volvo', 'iveco', 'daf']
print(truck)
truck.remove('daf')
print(truck)

too_expensive = 'scania'
truck.remove(too_expensive)
print(truck)
print(f"\nTa cięzarówka {too_expensive.title()} jest za droga")


#3.4
goscie = ['adam', 'jacek', 'grzegorz', 'marta', 'vika']
print(f"Zapraszam {goscie[0].title()}")
print(f"Zapraszam {goscie[2].title()}")
mess=f"Nie moze przyjsc {goscie[3].title()}"
print(mess)

goscie[3] = 'wiktor'
print(goscie)

print("Znaleziono nowy stół")
goscie.insert(3, 'bartek')
goscie.insert(0, 'grzegorz')
goscie.append('nikola')
print(goscie)
mess = f"witam cie {goscie[0].title()}"
print(mess)

len(goscie)
print(len(goscie))























































