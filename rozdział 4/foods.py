my_foods = ['pierogi',  'kurczak', 'makaron', 'spaghetti']
friend_foods = my_foods[:]   #kopia listy

my_foods.append('lody')
friend_foods.append('marchewka')

print("moje ulub jedz to")
print(my_foods)

print("\nUlub jedz kolegi to: " ,friend_foods)

print("3 pierw to: ", my_foods[:3])
print("srodek" , my_foods[2:4])
print("ostsatnie elem.", my_foods[-3:])



print("nasze ulubione jedzenie to: ")
for food in my_foods + friend_foods:
    print(f" - {food}")