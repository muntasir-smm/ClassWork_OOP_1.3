class Furniture:

    def __init__(self, material, price):
        self.material = material
        self.price = price

    def get_details(self):
        formatted_price = (
            int(self.price) if self.price.is_integer() else self.price
        )
        return f"{self.material}, ${formatted_price}"


class Chair(Furniture):

    def __init__(
        self, material, price, has_armrests, seat_height
    ):
        super().__init__(material, price)
        self.has_armrests = has_armrests
        self.seat_height = seat_height

    def get_details(self):
        armrests_str = "Armrests" if self.has_armrests else "No armrests"
        height_str = (
            f"{int(self.seat_height)}cm"
            if self.seat_height.is_integer()
            else f"{self.seat_height}cm"
        )
        return f"{super().get_details()}, {armrests_str}, {height_str}"


class Table(Furniture):

    def __init__(self, material, price, shape, leg_count):
        super().__init__(material, price)
        self.shape = shape
        self.leg_count = leg_count

    def get_details(self):
        return f"{super().get_details()}, {self.shape}, {self.leg_count} legs"


# Test implementation
chair = Chair(material="Wood", price=200.0, has_armrests=True, seat_height=45.0)
table = Table(material="Glass", price=300.0, shape="Rectangular", leg_count=4)

print(chair.get_details())
print(table.get_details())