class Pet:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_description(self):
        formatted_price = (
            int(self.price) if self.price.is_integer() else self.price
        )
        return f"{self.name}, ${formatted_price}"


class Dog(Pet):

    def __init__(self, name, price, breed, weight):
        super().__init__(name, price)
        self.breed = breed
        self.weight = weight

    def get_description(self):
        return f"{super().get_description()}, {self.breed}, {self.weight}kg"


class Cat(Pet):

    def __init__(self, name, price, color, is_indoor: bool):
        super().__init__(name, price)
        self.color = color
        self.is_indoor = is_indoor

    def get_description(self):
        indoor_str = "Indoor" if self.is_indoor else "Outdoor"
        return f"{super().get_description()}, {self.color}, {indoor_str}"


# Test implementation
dog = Dog(name="Buddy", price=500.0, breed="Labrador", weight=30.5)
cat = Cat(name="Whiskers", price=300.0, color="Black", is_indoor=True)

print(dog.get_description())
print(cat.get_description())