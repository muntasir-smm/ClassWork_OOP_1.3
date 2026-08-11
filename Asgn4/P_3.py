class Pet:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_description(self):
        return (f"{self.name}, ${self.price}")


class Dog(Pet):

    def __init__(self, name, price, breed, weight):
        Pet.__init__(self,name, price)
        self.breed = breed
        self.weight = weight

    def get_description(self):
        return (f"{self.name}, ${self.price}, {self.breed}, {self.weight} Kg")


class Cat(Pet):

    def __init__(self, name, price, color, is_indoor):
        Pet.__init__(self,name, price)
        self.color = color
        self.is_indoor = is_indoor

    def get_description(self):
        return (f"{self.name}, ${self.price}, {self.color}, {"Indoor" if self.is_indoor==True else "Outdoor"}")


def main():
    Dog1= Dog("Buddy",500.0,"Labrador",30.5)
    print(Dog1.get_description())
    Cat1=Cat("Whiskers",300.0,"Black",True)
    print(Cat1.get_description())

main()