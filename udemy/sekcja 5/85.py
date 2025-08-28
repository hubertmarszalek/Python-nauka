def displayShoppingList(shoppingList):
    print("Shopping list: ")
    for item in shoppingList:
        print(f"- {item}")


shoppingList = []
while True:
    operacja = input("dodaj zakupy lub koniec: ")
    if operacja == "koniec":
        displayShoppingList(shoppingList)
        break

    elif operacja == "dodaj":
        rzecz = input("co chcesz dodac?: ")
        shoppingList.append(rzecz)
        print(f"dodano {rzecz}")
    else:
        print("nieznana komenda")