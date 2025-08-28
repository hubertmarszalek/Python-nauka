favourite_book = ['Hobbit', 'Metro 2033', 'Pies', 'Latarnik']
for book in favourite_book:
    print(f"jedna z ulub ksiazek to: {book}")
print('Lubie czytac')


friend_fv_book = favourite_book[:]
print("jego ulubione książki to: ")
for book in friend_fv_book:
    print(f" - {book}")

friend_fv_book.sort()
print(friend_fv_book)

for book in friend_fv_book:
    print(book.upper())