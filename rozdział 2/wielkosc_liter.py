#2.3
imie = "Eryk"
print(f"Witaj, {imie}")

#2.4
imie_1 = "Adam"
print(imie.upper())
print(imie.lower())
print(imie.title())

#2.5
text_1 = "Albert Einstein powiedział kiedyś:"
text_2 = ' "cos tam bla bla"'
fulltext = text_1 + text_2
print(fulltext)

#2.6
famous_people = "Einstein"
message = f'{famous_people} powiedział kiedyś: "cos tam bla bla"'
print(message)

#2.7

imie_2 = "\n\txFilipx"
print(imie_2)
imie_3 = " Filip "
print(imie_3.lstrip())
print(imie_3.rstrip())
print(imie_3.strip())