class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library(Book):

    def __init__(self, title, author):
        super().__init__(title, author)
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return "Book added succesfully"

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        else:
            return "There is no such book in library"
