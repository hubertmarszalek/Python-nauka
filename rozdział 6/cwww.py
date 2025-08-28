favorite_languages = {
    'Adam': 'Python',
    'Ola': 'JavaScript',
    'Ewa': 'C++'
}

friends = ['Ola', 'Ewa', 'Marek']


for friend in friends:
    if friend in favorite_languages:
        print(f"czesc {friend.title()} widze ze lubisz {favorite_languages[friend.title()]} ")
    else:
        print(f"czesc {friend} widze ze nie podales ")

animal_sounds = {
        'pies': 'hau hau',
        'kot': 'miau',
        'krowa': 'muuu',
        'kura': 'ko ko ko'
    }

farm_animals = ['kot', 'pies', 'koń', 'krowa']
for animal in farm_animals:
    if animal in animal_sounds:
        print(f"Zwierze {animal} mowi {animal_sounds[animal]}")
    else:
        print(f"{animal} nie wiem jaki ma dzwiek")




favorite_subjects = {
    'Ania': 'matematyka',
    'Bartek': 'biologia',
    'Celina': 'fizyka',
    'Dawid': 'informatyka'
}

present_students = ['Bartek', 'Celina', 'Ewa', 'Ania']
for present_student in present_students:
    if present_student in favorite_subjects:
        print(f"{present_student} lubisz {favorite_subjects[present_student]}")
    else:
        print(f"{present_student} nie podales przedmiotu")

for student in favorite_subjects:
    if student not in present_students:
        print(f"{student} nie ma go")











































































