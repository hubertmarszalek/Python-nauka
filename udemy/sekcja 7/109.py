# symulacja kosztów podróży

import math
import random

dystans = random.randint(100, 1000)
print("dystans:", dystans)

spalanie = math.ceil(0.075*dystans)
print("spalone litry:", spalanie)


cena_paliwa = random.uniform(4.5, 5.5)
cena_paliwa = round(cena_paliwa,2)
print("cena:", cena_paliwa)

koszt_za_trase = spalanie * cena_paliwa
print(f"koszt_za_trase: {koszt_za_trase:.2f}")

if koszt_za_trase > 200:
    print("wysokie koszty podrózy")
else:
    print("przystępne koszty podróży")
