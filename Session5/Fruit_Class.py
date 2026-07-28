'''
Write Python programs for creating following classes and their objects:

14. Fruit Class

'''

class Fruit:
    def __init__(self,name,color,Price):
        self.name=name
        self.color=color
        self.Price=Price

def main():
    frt1=Fruit("Mango","Golden",120)
    print(f"Name:{frt1.name}\ncolor:{frt1.color}\nPrice: {frt1.Price}tk/kg")
main()
