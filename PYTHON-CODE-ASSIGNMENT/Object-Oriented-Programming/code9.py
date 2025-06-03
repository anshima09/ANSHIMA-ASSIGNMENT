class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

book1 = Book("1984", "George Orwell")
member1 = Member("Alice")
member1.borrow_book(book1)

for book in member1.borrowed_books:
    print(f"{member1.name} borrowed '{book.title}' by {book.author}")
