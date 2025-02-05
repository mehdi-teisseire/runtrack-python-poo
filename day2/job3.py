class Book:
    def __init__(self,title,page,author,in_stock):
        self.title__ = title
        self.page__ = page
        self.author__ = author
        self.in_stock__ = True
    def set_book_page(self,page):
        if page < 0:
            print("Error: We don't take Negative Numbers book page set to the previous value.")
        else:
            self.page__ = page
    def get_book_page(self):
        return self.page__
    def set_in_stock(self,in_stock):
        self.in_stock__ = in_stock
    def get_in_stock(self):
        return self.in_stock__
