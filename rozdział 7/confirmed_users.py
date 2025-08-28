# Lista użytkowników, którzy jeszcze nie zostali zweryfikowani
unconfirmed_users = ['alicja', 'adam', 'pawel']

# Pusta lista, do której będziemy przenosić potwierdzonych użytkowników
confirmed_users = []

# Pętla while będzie działała DOPÓKI lista unconfirmed_users nie jest pusta
while unconfirmed_users:
    # .pop() usuwa ostatni element z listy unconfirmed_users i przypisuje go do current_user
    current_user = unconfirmed_users.pop()

    # Wyświetlenie komunikatu o weryfikacji użytkownika
    print(f"Weryfikacja użytkownika {current_user.title()}")

    # Dodanie użytkownika do listy potwierdzonych
    confirmed_users.append(current_user)

# Po zakończeniu pętli (czyli gdy unconfirmed_users jest już pusta)
# wyświetlamy listę wszystkich potwierdzonych użytkowników
print("\nZweryfikowano poniżej podanych użytkowników:")
for user in confirmed_users:  # Dla każdego użytkownika w liście potwierdzonych
    print(user.title())       # Wyświetlamy jego imię z wielkiej litery
