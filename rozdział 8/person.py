def miejsce( kraj, miasto, kontynent='europa'):
    print(f"mieszkam na kontynencie {kontynent.title()} w {kraj.title()} miescie {miasto.title()}")


miejsce('polska', 'bielsko')
miejsce('japonia', 'Tokio', kontynent='azja')



def person(name,lastname, nick=''):
    if nick:
        fullname = f"{name} {nick} {lastname}"
    else:
        fullname = f"{name} {lastname}"
    return fullname




ktos = person('jack', 'joo')
print(ktos)
ktos2 = person('jack', 'mii', 'jung')
print(ktos2)



def build_person(firstname, lastname):
    """zwraca slownik informacji o danej osobie"""
    person = {'first': firstname, 'last': lastname}
    return person


musician = build_person('jack', 'mii')
print(musician)
print(person)




waga = float(input("Ile wazysz? "))
wzrost = float(input("Ile wzrost? "))


def bmi(waga, wzrost):
    bmii = (waga / wzrost**2)*10000
    print(f"Twoje bmi to: {bmii:.2f}")
    if bmii <= 17:
        print("wychudzenie")
    elif bmii <= 25:
        print("prawidlowo")
    elif bmii <= 30:
        print("nadwaga")
    else:
        print("otylosc")



bmi(waga, wzrost)







def build_person(firstname, lastname, age=None):
    """zwraca slownik informacji o danej osobie"""
    person = {'first': firstname, 'last': lastname}
    if age:
        person['age'] = age
    return person






def make_album(artysta, tytul, liczba=None):
    album = {'artysta': artysta,'tytul': tytul}
    if liczba:
        album['liczba'] = liczba
    return album


al = make_album('lady gaga', 'one', '23')
print(al)





def get_formatted_name(firstname, lastname):
    fullname = f"{firstname} {lastname}"
    return fullname

while True:
    print("podaj imie i nazwisko")
    f_name = input("podaj imie: ")
    if f_name == 'q':
        break

    print("podaj nazwisko")
    l_name = input("podaj nazwisko: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"formatted_name")





def full_student(firstname, lastname, age=None, oceny=None):
    student = {'first': firstname, 'last': lastname}
    if age:
        student['age'] = age
    if oceny:
        student['oceny'] = oceny
    return student

student1 = full_student('jack', 'mii')
print(student1)
student2 = full_student('jack', 'mii', age=18, oceny=[2,6,3])
print(student2)



def bilans_uczniow(imie, nazwisko, waga, wzrost):
    uczen = {'imie': imie, 'nazwisko': nazwisko, 'waga': waga, 'wzrost': wzrost}

    bmi = waga / (wzrost**2)

    uczen['bmi'] = f"{bmi:.4f}"  # wynik będzie typu str

    return uczen

uczen1 = bilans_uczniow('jack', 'mii', 87, 175)
print(uczen1)




operacja = input("operacja (+, -, *, /): ")
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











