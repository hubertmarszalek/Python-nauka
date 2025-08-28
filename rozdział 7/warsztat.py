car_repairs = ['opony', 'hamulce', 'klima', 'hamulce', 'silnik']

finished_repairs = []

while 'hamulce' in car_repairs:
    car_repairs.remove('hamulce')
    print("Przepraszamy nie mamy takiej częsci")

while car_repairs:
    finished_repair = car_repairs.pop()
    print("naprawa w toku")

    finished_repairs.append(finished_repair)

print("zakonczono naprawy")
for repair in finished_repairs:
    print(repair)