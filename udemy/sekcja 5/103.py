# zarządzanie stanem konta użytkownikow

accountBalance = 0

def addFunds():
    add = float(input("dodaj kase "))
    global accountBalance
    accountBalance += add
    print(accountBalance)


def withdrawFunds():
    cashout = float(input("wyplac kase "))
    global accountBalance
    if cashout > accountBalance:
        print("brak wystarczajacych srodkow")
    elif cashout <= accountBalance:
        accountBalance -= cashout

def displayBalance():
    global accountBalance
    print(accountBalance)



while True:
    action = input("bankomat (wpłata, wypłata, stan)")
    if action == "wpłata":
        addFunds()
    elif action == "stan":
        displayBalance()
    elif action == "wypłata":
        withdrawFunds()
    else:
        print(f"twoje saldo to: {accountBalance}")
        break


