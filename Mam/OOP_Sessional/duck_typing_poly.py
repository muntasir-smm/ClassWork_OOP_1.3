class Dog:
    def speak(self):
        return "ghew ghew!"
    def move(self):
        return "Runs on four legs"
class Robot:
    def speak(self):
        return "Beep beep!"
    def move(self):
        return "Rolls on wheels"
class Human:
    def speak(self):
        return "Hello!"
    def move(self):
        return "Walks on two legs"
# Polymorphic function
def describe_entity(obj):
    print(f"Sound: {obj.speak()}")
    print(f"Movement: {obj.move()}")
    print()
# Testing with different objects
dog = Dog()
robot = Robot()
human = Human()
describe_entity(dog)
describe_entity(robot)
describe_entity(human)