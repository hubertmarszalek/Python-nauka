# walidacja maila 1

def validateEmail(email):
    monkeyIndex = email.find('@')
    dotIndex = email.find('.')
    if monkeyIndex == -1 or dotIndex == -1:  # -1 = brak
        return False
    else:
        return True


email1 = 'asia@example.com'
print(validateEmail(email1))

email2 = 'asiaexample.com'
print(validateEmail(email2))


# walidacja maila 2

def validateEmail2(email):
    monkeyIndex = email.find('@')
    dotIndex = email.find('.')

    if monkeyIndex == -1:
        return 'brakuje "@" '
    elif dotIndex == -1:
        return 'brakuje "." '
    elif monkeyIndex > dotIndex:
        return 'zła koljenośc'
    else:
        return 'mail poprawny'


email3 = 'asia@example.com'
print(validateEmail2(email3))

email4 = 'asiaexample.com'
print(validateEmail2(email4))

email5 = 'mail@pl'
print(validateEmail2(email5))

email6 = 'mail.@pl'
print(validateEmail2(email6))
