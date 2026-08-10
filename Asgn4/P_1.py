class Vehicle:

    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def get_info(self) -> str:
        return f"{self.brand}, {self.year}"


class Car(Vehicle):

    def __init__(self, brand: str, year: int, num_doors: int, fuel_type: str):
        super().__init__(brand, year)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.num_doors} doors, {self.fuel_type}"


class Motorcycle(Vehicle):

    def __init__(
        self, brand: str, year: int, has_sidecar: bool, engine_size: int
    ):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar
        self.engine_size = engine_size

    def get_info(self) -> str:
        sidecar_str = "Sidecar" if self.has_sidecar else "No sidecar"
        return f"{super().get_info()}, {sidecar_str}, {self.engine_size}cc"


# Test implementation
car = Car(brand="Toyota", year=2020, num_doors=4, fuel_type="Petrol")
motorcycle = Motorcycle(
    brand="Honda", year=2021, has_sidecar=False, engine_size=500
)

print(car.get_info())
print(motorcycle.get_info())