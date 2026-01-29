class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year

    def printData(self):
        print(self.title)
        print(self.author)
        print(self.isbn)
        print(self.year)

book1 = Book("Book 1", "<NAME>", "1999", 1999)
book1.printData()

book2 = Book("Book 2", "<NAME>", "1999", 1999)
book2.printData()