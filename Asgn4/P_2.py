class LibraryItem:

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    def check_availability(self):
        return (f"{self.title} is available")


class Book(LibraryItem):

    def __init__(self, title, item_id, author, pages):
        LibraryItem.__init__(self,title, item_id)
        self.author = author
        self.pages = pages

    def check_availability(self):
        return (f"{self.title} by {self.author} is available")


class DVD(LibraryItem):

    def __init__(self, title, item_id, director, duration):
        LibraryItem.__init__(self,title, item_id)
        self.director = director
        self.duration = duration

    def check_availability(self):
        return (f"{self.title} by {self.director} is available")


def main():
   Book1=Book("Python Basics","B123","John Smith",300)
   print(Book1.check_availability())
   DVD1=DVD("Python Tutorial","D456","Jane Doe",120)
   print(DVD1.check_availability())
   

main()