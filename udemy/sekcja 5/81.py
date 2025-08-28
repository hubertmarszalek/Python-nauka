def createUser(name,contact):
    user = {
        'name': name,
        'email': None,
        'phone': None,
    }
    if isinstance(contact, int):
        user['phone'] = contact
    elif isinstance(contact, str):
        user['email'] = contact

    return user



user1 = createUser("adam","adam@wp.pl")
print(user1)

user2 = createUser("adam",122333444)
print(user2)
