#lista ze zbanowanymi osobami , program sprawdza czy dany uzykownik nie jest zbanoiwany
banned_user = ['Adam', 'Oliwier', 'Tom', 'Bot']
user = 'maria'
if user not in banned_user:
    print(f"{user.title()} mozesz publikowac ")


car = 'audi'
print("Czy car == 'subaru'?")
print(car == 'subaru')