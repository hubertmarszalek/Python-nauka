n = int(input("PODAJ LICZBE N"))
list = []
for i in range(1,n + 1):
    list.append(i ** 2)

print(f'lista kwadratow liczb od 1 do n: {list}')