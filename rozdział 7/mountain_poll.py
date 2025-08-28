responses = {}  # pusty słownik, w którym będziemy zapisywać odpowiedzi uczestników (klucz = imię, wartość = szczyt)

polling_active = True  # flaga sterująca pętlą; dopóki jest True, pytamy kolejnych uczestników

while polling_active:  # "dopóki ankieta jest aktywna"
    name = input("\nJak masz na imie? ")  # pytamy użytkownika o imię
    response = input("Na który szczyt się wybierasz")  # pytamy o szczyt, na który chce wejść

    responses[name] = response  # zapisujemy odpowiedź w słowniku: imię jako klucz, szczyt jako wartość

    repeat = input("Czy ktokolwiek inny chce wziąć udział w ankiecie? (tak / nie)")  # pytamy, czy kontynuować
    if repeat == 'nie':  # jeśli odpowiedź to 'nie', przerywamy ankietę
        polling_active = False  # ustawiamy flagę na False, co zatrzyma pętlę

# Po zakończeniu pętli wyświetlamy wszystkie zebrane odpowiedzi
print("\n---Wyniki ankiety---")
for name, response in responses.items():  # .items() daje pary (klucz, wartość)
    print(f"{name} chciałby się wspiąć na {response}")  # wypisujemy w formacie "Imię + szczyt"
