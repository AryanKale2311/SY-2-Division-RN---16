
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print("Patron registered successfully")

    def borrow_book(self, book_id, patron_id):
        for book in self.books:
            if book.book_id == book_id and book.available:
                for patron in self.patrons:
                    if patron.patron_id == patron_id:
                        book.available = False
                        patron.borrowed_books.append(book)
                        print("Book borrowed successfully")
                        return

        print("Book or patron not found, or book unavailable")

    def return_book(self, book_id, patron_id):
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                for book in patron.borrowed_books:
                    if book.book_id == book_id:
                        book.available = True
                        patron.borrowed_books.remove(book)
                        print("Book returned successfully")
                        return

        print("Book not found in patron's records")


library = Library()

b1 = Book(1, "Python Programming", "Guido")
b2 = Book(2, "Data Structures", "Mark Allen")

p1 = Patron("Aryan", 101)

library.add_book(b1)
library.add_book(b2)

library.register_patron(p1)

library.borrow_book(1, 101)
library.return_book(1, 101)
