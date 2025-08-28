cars = {
    'ford': 'fiesta',
    'audi': 'a3',
    'hyundai': 'ix20'

}
for car, model in cars.items():
    print(f"Marki to:{car}")

for model in cars.values():
    print(f"Marki to:{model}")

for car in sorted(cars):
    print(f"Marki to:\n{car}")


favourite_languages = {
    'jen': 'Python',
    'sar': 'C',
    'edu': 'Python',
    'edek': 'C',
    'uni': 'Java'
}
ankietowani = ['jen', 'sar', 'edu', 'uni']

osoby = favourite_languages.keys()
for osoba in favourite_languages:
    if osoba in ankietowani:
        print(f"Wziąłes udział {osoba}")
    else:
        print(f"{osoba} nie znaleziony")