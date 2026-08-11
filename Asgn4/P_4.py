class Furniture:

    def __init__(self, material, price):
        self.material = material
        self.price = price

    def get_details(self):
        return f"{self.material}, ${self.price}"


class Chair(Furniture):

    def __init__(
        self, material, price, has_armrests, seat_height
    ):
        Furniture.__init__(self,material, price)
        self.has_armrests = has_armrests
        self.seat_height = seat_height

    def get_details(self):
        return f"{self.material}, ${self.price},{"Armrests" if self.has_armrests==True else "No Armrests"}, {self.seat_height} cm"


class Table(Furniture):

    def __init__(self, material, price, shape, leg_count):
        Furniture.__init__(self,material, price)
        self.shape = shape
        self.leg_count = leg_count

    def get_details(self):
        return f"{self.material}, ${self.price}, {self.shape},{self.leg_count} legs"


def main():
    Chair1=Chair("Wood",200.0,True,45.0)
    print(Chair1.get_details())
    
    Table1=Table("Glass",300.0,'Rectengular',4)
    print(Table1.get_details())

main()