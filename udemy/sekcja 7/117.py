
guests = ['adam','ela','ania','bartek','grzegorz']
print(f"Liczba gości: {len(guests)}")

guests.extend(['rafal', 'oliwier'])

del guests[3]  # usuniecie #3 - bartka
print(guests)

guests.sort()
print(guests)

dishes = ['ryba','pizza','kurczak']
dishes.append('ziemniaki')
dishes.append('salatka')
print(dishes)

middle_dishes = dishes[len(dishes) // 2]
print(middle_dishes)

dishes.pop()
print(dishes)

if 'pizza' in dishes:
    print("pizza jest na liscie")
else:
    dishes.append('pizza')