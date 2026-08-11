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