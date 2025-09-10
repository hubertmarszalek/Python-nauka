adressBook = {'jan kowalski' : {'miasto':'bielsko', 'kod':'43-300'}}
print(adressBook)

adressBook['adam'] = {'miasto':'gdansk', 'kod':'80-000'}
print(adressBook)

del adressBook['jan kowalski']
print(adressBook)

adressBook_copy = adressBook.copy()
print(adressBook_copy)



found = False
for person in adressBook.values():
    if person["miasto"] == 'krakow':
        found = True
        print('jest osoba z krakowa')

if not found:
    print('nie ma osoby z krakowa')


print(adressBook.keys())
print(adressBook.values())