grades = {
    'Ania': 95,
    'Bartek': 67,
    'Celina': 83,
    'Dawid': 42,
    'Ewa': 74,
    'Filip': 59
}
for student in grades:
    if grades[student] >= 70:
        print(f"{student} bdb")


oceny_5 = []
for student in grades:
    if grades[student] >= 70:
        oceny_5.append(student)

print(oceny_5)