def ugotuj_skladnik(skladnik):
    ugotowany_skladnik = skladnik.replace('surowe', 'ugotowane')
    ugotowany_skladnik = ugotowany_skladnik.replace('surowa', 'ugotowana')
    ugotowany_skladnik = ugotowany_skladnik.replace('surowy', 'ugotowany')
    return ugotowany_skladnik

def gotuj(*args, przyprawa):
    print(f"uzywam przyprawy {przyprawa}")
    ugotowane_skladniki = []
    for skladnik in args:
        ugotowane_skladniki.append(ugotuj_skladnik(skladnik))
    return ugotowane_skladniki

surowe = [
    "surowy makaron",
    "surowa marchewka",
    "surowe ziemniaki",
]

wynik = gotuj(*surowe, przyprawa="bazylia")
print(wynik)
