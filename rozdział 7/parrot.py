message = input("Podaj swoje imie")
print(f"moje imie to {message}")



prompt = "jezeli powiesz nam kim jestes ... komunikat"
prompt += "\nnapisz 'koniec' aby zakonczyc "
message = ""
while message != 'koniec':
    message = input(prompt)
    if message != 'koniec':
        print(message)




prompt = "jezeli powiesz nam kim jestes ... komunikat"
prompt += "\nnapisz 'koniec' aby zakonczyc "

active = True
while active:
    message = input(prompt)
    if message == 'koniec':
        active = False
    else:
        print(message)



prompt = "dodaj bilety do koszyka: darmowy, ulgowy, normalny, senior"
prompt += "\nNapisz 'koniec' aby zakonczyc zamowineie"

active = True
while active:
    message = input(prompt)
    if message == 'koniec':
        active = False
    else:
        print(f"dziekujemy za zakup biletu: {message}")


active = True
wiek = input("")