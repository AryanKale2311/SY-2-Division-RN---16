class Library:
    def __init__(self):
        self.books = {
            "Python": True,
            "Java": True,
            "C++": True
        }
        self.patrons = []

    def add_patron(self):
        name = input("Enter patron name: ")
        self.patrons.append(name)
        print(name, "added successfully!")

    def borrow_book(self):
        book = input("Enter book name: ")
        if book in self.books and self.books[book]:
            self.books[book] = False
            print("Book borrowed successfully!")
        else:
            print("Book is not available.")

    def return_book(self):
        book = input("Enter book name: ")
        if book in self.books:
            self.books[book] = True
            print("Book returned successfully!")
        else:
            print("Book not found in library.")

    def show_books(self):
        print("\nAvailable Books:")
        for book, available in self.books.items():
            if available:
                print("-", book)


library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add New Patron")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Show Available Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_patron()
    elif choice == 2:
        library.borrow_book()
    elif choice == 3:
        library.return_book()
    elif choice == 4:
        library.show_books()
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("Invalid choice.")