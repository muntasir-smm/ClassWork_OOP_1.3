class Vehicle:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_info(self):
        return (f"{self.brand}, {self.year}")


class Car(Vehicle):

    def __init__(self, brand, year, num_doors, fuel_type):
        Vehicle.__init__(self,brand, year)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def get_info(self):
        return (f"{self.brand}, {self.year}, {self.num_doors} doors, {self.fuel_type}")


class Motorcycle(Vehicle):

    def __init__(self, brand, year, has_sidecar, engine_size):
        Vehicle.__init__(self,brand, year)
        self.has_sidecar = has_sidecar
        self.engine_size = engine_size

    def get_info(self):
            return (f"{self.brand}, {self.year},{"No sidecar" if self.has_sidecar==False else "Has sidecar" },{self.engine_size}cc")

def main():
    car1 = Car("Toyota", 2020, 4, "Petrol")
    motorcycle1 = Motorcycle("Honda", 2021, True, 500)
    print(car1.get_info())
    print(motorcycle1.get_info())

main()