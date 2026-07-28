'''
Write Python programs for creating following classes and their objects:

8. Food Class

'''

class Food:
    def __init__(self,name,Type,Price):
        self.name=name
        self.Type=Type
        self.Price=Price

def main():
    foo1=Food("Kachhi","Fresh","3.7K")
    print(f"Name:{foo1.name}\nType:{foo1.Type}\nPrice: {foo1.Price}")
main()
