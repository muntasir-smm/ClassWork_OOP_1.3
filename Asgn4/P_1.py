class Vehicle:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_info(self):
        return f"{self.brand}, {self.year}"


class Car(Vehicle):

    def __init__(self, brand, year, num_doors, fuel_type):
        Vehicle.__init__(self,brand, year)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def get_info(self):
        return f"{self.brand}, {self.year}, {self.num_doors} doors, {self.fuel_type}"


class Motorcycle(Vehicle):

    def __init__(
        self, brand, year, has_sidecar, engine_size
    ):
        Vehicle.__init__(self,brand, year)
        self.has_sidecar = has_sidecar
        self.engine_size = engine_size

    def get_info(self):
            return f"{self.brand}, {self.year},{"No" if self.has_sidecar==False else "Has sidecar" } sidecar,{self.engine_size}cc"

car = Car(brand="Toyota", year=2020, num_doors=4, fuel_type="Petrol")
motorcycle = Motorcycle(
    brand="Honda", year=2021, has_sidecar=False, engine_size=500
)

print(car.get_info())
print(motorcycle.get_info())