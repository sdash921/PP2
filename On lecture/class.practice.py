class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def borrow(self):
        self.is_borrowed = True
    def return_book(self):
        self.is_borrowed = False

def get_available_books(book_list):
    available = []
    for book in book_list:
        if not book.is_borrowed:
            available.append(book)
    return available

# --- Testing your code ---
b1 = Book("1984", "George Orwell")
b2 = Book("The Hobbit", "J.R.R. Tolkien")
b3 = Book("The Road", "Cormac McCarthy")

# Let's pretend someone borrows '1984'
b1.borrow()

library = [b1, b2, b3]
available = get_available_books(library)

print("Available books:")
for b in available:
    print(b)