from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    @abstractmethod
    def getsound(self):
        pass

class Dog(Animal):
    def __init__(self, name, speed):
        Animal.__init__(self, name, speed)
    def getsound(self):
        print("ghew ghew")
class Cat(Animal):
    def __init__(self, name, speed):
        Animal.__init__(self, name, speed)
        #you can also use super().__init__(name, speed)

dog1 = Dog("Kitmir", 50)
print(dog1.name)
dog1.getsound()