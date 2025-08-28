pizza = ['pepperoni', 'roma', 'ananas']

friend_pizzas = pizza[:]
pizza.append('roma')
friend_pizzas.append('margheritta')
print(friend_pizzas)
print(pizza)


print("moje ulubione pizze to: ")
for p in pizza:
    print(f" - {p}")

print("ulubione pizze przyjaciela to: ")
for p in friend_pizzas:
    print(f" - {p}")