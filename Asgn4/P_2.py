class LibraryItem:

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    def check_availability(self):
        return f"{self.title} is available"


class Book(LibraryItem):

    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def check_availability(self):
        return f"{self.title} by {self.author} is available"


class DVD(LibraryItem):

    def __init__(
        self, title, item_id, director, duration
    ):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration

    def check_availability(self):
        return f"{self.title} by {self.director} is available"


# Test implementation
book = Book(
    title="Python Basics", item_id="B123", author="John Smith", pages=300
)
dvd = DVD(
    title="Python Tutorial", item_id="D456", director="Jane Doe", duration=120
)

print(book.check_availability())
print(dvd.check_availability())