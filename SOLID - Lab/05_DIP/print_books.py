class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class PyPrinter:
    @staticmethod
    def format(formatter):
        return f"---------{formatter.content} flier"


class Printer:
    def get_book(self, book: Book, formater):
        formatter = formater
        formatter.format(book)
        return formatter.format(book)


p1 = Printer()
p2 = Printer()
b = Book("Tittle1")

normal = Formatter()
flier = PyPrinter()

print(p1.get_book(b, normal))
print(p2.get_book(b, flier))
