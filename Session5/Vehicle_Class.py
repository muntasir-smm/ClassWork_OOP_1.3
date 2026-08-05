'''
Write Python programs for creating following classes and their objects:
1. Vehicle Class

'''

class Vehicle:
    def __init__(self,brand,model,color,price):
        self.brand=brand
        self.model=model
        self.color=color
        self.price=price
    

def main():
    BMW=Vehicle("BMD","007","Black","$1.5M")
    print(f"Brand: {BMW.brand}\nModel: {BMW.model}\nColor: {BMW.color}\nPrice: {BMW.price}")

main()