class Book:
    def __init__(self,title,page,author):
        self.title__ = title
        self.page__ = page
        self.author__ = author
    def set_book_page(self,page):
        if page < 0:
            print("Error: We don't take Negative Numbers book page set to the previous value.")
        else:
            self.page__ = page
    def get_book_page(self):
        return self.page__

book = Book("The Great Gatsby", 200, "F. Scott Fitzgerald")
print(book.get_book_page())
book.set_book_page(300)
print(book.get_book_page())
book.set_book_page(-300)
print(book.get_book_page())