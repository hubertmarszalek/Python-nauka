user = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'maria',
        'last': 'curie',
        'location': 'paris',
    }
}
for username, user_info in user.items():
    print(f"Username: {username}")
    full_name = user_info['first']  +" "+ user_info['last']
    print(f"Full name: {full_name}")
    location = user_info['location']

    print(f"\timie i nazwisko: {full_name.title()}")
    print(f"\tlokalizacja: {location.title()}")