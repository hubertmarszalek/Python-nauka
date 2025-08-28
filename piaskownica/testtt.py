
while True:
    operacja = input("operacja (+, -, *, /, stop): ")

    if operacja == "stop":
        break

    liczba1 = int(input("liczba 1: "))
    liczba2 = int(input("liczba 2: "))



    if operacja == '+':
        operacja = liczba1 + liczba2
        print(operacja)
    if operacja == '-':
        operacja = liczba1 - liczba2
        print(operacja)
    if operacja == '*':
        operacja = liczba1 * liczba2
        print(operacja)
    if operacja == '/':
        operacja = liczba1 / liczba2
        print(operacja)
    else:
        print("blad")

