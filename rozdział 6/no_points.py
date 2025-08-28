alien_0 = {'color': 'green', 'szybkosc': 5}
#print(alien_0['points'])

point_value = alien_0.get('points', 'Brak przypisanych pkt')
print(point_value)




osoby = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 18,
    'city': 'Springfield',

}
for key, value in osoby.items():
    print(key,':', value)




favourite_numbers = {
    'john': '6',
    'axel': '7'
}
for key, value in favourite_numbers.items():
    print(f"Ulubione liczby to\n {key,':', value}")





favourite_numbers = {
    'john': '6',
    'axel': '7'
}
print("Ulubione liczby to:")
for key, value in favourite_numbers.items():
    print(key,':', value)






slownik = {
    'python':'\njezyk programowania',
    'django': '\nframework',
    'komentarz': '\nTekst w kodzie, który nie jest wykonywany'
}
for key, value in slownik.items():
    print(key,':', value)