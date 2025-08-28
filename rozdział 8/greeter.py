def greet_user(username):
    """Wyświetla proste powitanie"""
    print(f"Witaj {username}")

greet_user('janek')


def dispaly_messages(language):
    print(f"Ucze sie {language}")

dispaly_messages('python')



def powitanie(jak, kto):
    print(jak + ", " + kto + "!")


powitanie("hej", "python")



def suma(a, b):
    print("wynik to", + a + b)

suma(1, 2)


def wypisz_od_a_do_b(a, b):
    for liczba in range(a, b + 1):
        print(liczba)


wypisz_od_a_do_b(5, 13)




def describe_pet(animal_type, pet_name):
    print(f"\nMoje zwierze to {animal_type}.")
    print(f"Mój {animal_type} nazywa sie {pet_name.title()}.")

describe_pet("pies", "bury")
describe_pet("kot", "kotencja")







def describe_pet(pet_name, animal_type='pies'):
    print(f"\nMoje zwierze to {animal_type}.")
    print(f"Mój {animal_type} nazywa sie {pet_name.title()}.")

describe_pet(pet_name="rocky")

def make_shirt(rozmiar, nadruk):
    print(f"\nChce kupic koszulke {rozmiar} z nadrukiem '{nadruk}'.")

make_shirt("L", "MARVEL")
make_shirt("S", "Super")






def make_shirt(rozmiar='XL', nadruk='Kocham pythona'):
    print(f"\nChce kupic koszulke {rozmiar} z nadrukiem '{nadruk}'.")


make_shirt()
make_shirt(rozmiar='L')
make_shirt(rozmiar='S', nadruk='Kocham jave')



def describe_city(miasto, kraj='Polska'):
    print(f"\n{miasto.title()} lezy w kraju {kraj.title()}.")


describe_city("bielsko")
describe_city("praga", "czechy")


















