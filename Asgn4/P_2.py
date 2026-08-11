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


def main():
   Boi=Book("Python Basics","B123","John Smith",300)
   print(Boi.check_availability())
   video_dekho=DVD("Python Tutorial","D456","Jane Doe",120)
   print(video_dekho.check_availability())
   

main()