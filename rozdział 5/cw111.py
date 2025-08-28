available_products = ['milk', 'bread', 'eggs', 'cheese', 'butter']
order = ['milk', 'beer','cheese','butter']
for product in order:
    if product in available_products:
        print(f"Dodano {product} do zamowienia")
    elif product == 'beer':
        print("nie sprzedajemy alkoholu")
    else:
        print(f"{product} nie dostepny")



users = ['ams', 'login', 'admin','mam','sas']
for user in users:
    if 'admin' in user:
        print("Witaj admin, jakie zad")
    else:
        print(f"Witaj {user}")




current_users = ['adam', 'admin','zodia','nuria','mel']
new_users = ['adam', 'los','kol','grl', 'Mel']

#tw listy kt porownuje male nazwy do siebie
current_users_lower = [user.lower() for user in current_users]

for new in new_users:
    if new.lower() in current_users_lower:     #porwnanie 1 listy malymi literami do nowej malymi lower()
        print(f"nazwa {new} została uzyta")
    else:
        print(f"Nazwa {new} jest dostepna")


numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")



grades = [55, 78, 89, 45, 92, 67, 88, 73, 100, 84, 60]
for grade in grades:
    if grade < 60:
        print(f"Ocena {grade} ndst")
    if grade >= 60 and grade <= 79:
        print(f"Ocena {grade} dost")
    if grade > 80:
        print(f"Ocena {grade} bdb")

print(sum(grades)/len(grades))
