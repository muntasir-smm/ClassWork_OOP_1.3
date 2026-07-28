'''
Write Python programs for creating following classes and their objects:
1. Vehicle Class
2. Circle Class
3. Rectangle Class
4. Triangle Class
5. Student Class
6. Employee Class
7. Teacher Class
8. Food Class
9. Temperature Class
10. Book Class
11. Movie Class
12. Person Class
13. Flower Class
14. Fruit Class
15. Animal Class
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