class Library:
    def __init__(self, books):
        self.books = books

    def List_books(self):
        print("Available books:")
        for book in self.books:
            print(book)

    def borrow_book(self,book_name):
        if book_name in self.books:
            print("Get your book now")
            self.books.remove(book_name)
        else:
            print("Book not available")

    def receive_book(self, returned_book):
        print("You have returned the book")
        self.books.append(returned_book)

books = ['English', 'History', 'Politics']
o = Library(books)
msg = """
      1. Display books 
      2. Borrow book
      3. Return book
      """
while True:
    print(msg)
    Ch = int(input("Enter your choice: "))
    if Ch == 1:
        o.List_books()
    elif Ch == 2:
        book_name = input("Enter the book you want to borrow: ")
        o.borrow_book(book_name)
    elif Ch == 3:
        returned_book = input("Enter the book you are returning: ")
        o.receive_book(returned_book)
    else:
        print("Thank You")
        quit()
