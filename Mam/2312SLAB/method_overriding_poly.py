class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a generic sound"
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