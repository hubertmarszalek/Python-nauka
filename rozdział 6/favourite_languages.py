favorite_languages = {
    'jen': 'python',
    'sar': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['jen'].title()

print(f"Ulubionym jezykiem jen jest: {language}")


for name, language in favorite_languages.items():
    print(f"\nUlubionym językiem {name} jest jezyk {language.title()}")

for name in favorite_languages.keys():
    print(name.title())

for language in favorite_languages.values():
    print(language.title())


friends = ['jen', 'sar']
for name in favorite_languages.keys():
    print(f"{name.title()}")
    language2 = favorite_languages[name]
    if name in friends:
        print(f"Witaj {name.title()} twoim ulubionym jezykiem jest {language2.title()}")

#sortowanie
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}")

#wypisuje wart bez powtarzania
for language in set(favorite_languages.values()):
    print(language.title())