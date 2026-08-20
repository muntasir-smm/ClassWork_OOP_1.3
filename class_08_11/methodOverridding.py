class Vehicle:
    def __init__(self, brand, type):
        self.brand = brand
        self.type = type

    def get_info(self):
        return (f"{self.type}: {self.brand}")


class Car(Vehicle):
    def get_info(self):
        return (f"{self.type}: {self.brand}")


class Motorcycle(Vehicle):
    def get_info(self):
        return (f"{self.type}: {self.brand}")

def main():
    car1 = Car("Toyota", "Car")
    motorcycle1 = Motorcycle("Honda", "Bike")
    print(car1.get_info())
    print(motorcycle1.get_info())

main()

# ::::::::::::::::::::::::::::::::::::::::

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes any sound"
    def eat(self):
        return f"{self.name} eats food"
class Lion(Animal):
    def speak(self):
        return f"{self.name} roars loudly!"
    def eat(self):
        return f"{self.name} eats meat"
class Elephant(Animal):
    def speak(self):
        return f"{self.name} trumpets!"
    def eat(self):
        return f"{self.name} eats plants"
lion = Lion("Simba")
animal = Animal("Anyanimal")
elephant = Elephant("Manny")
print(animal.speak())
print(animal.eat())
print()
print(lion.speak())
print(lion.eat())
print()
print(elephant.speak())
print(elephant.eat())
