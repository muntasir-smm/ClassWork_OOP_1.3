class Dog:
    def speak(self):
        return("Ghew Ghew")
    def move(self):
        return("Runs on four leg")
class Cat:
    def speak(self):
        return("Mew Mew")
    def move(self):
        return("Runs on four leg")
    
class Robot:
    def speak(self):
        return("Beep Beep")
    def move(self):
        return("Roll on wheel")
class Human:
    def speak(self):
        return("Hello...")
    def move(self):
        return("Walks on 7 leg")

def describe(munna):
    print(f"Sound: {munna.speak()}")
    print(f"Movement: {munna.move()}")
    print()

def main():
    dog=Dog()
    cat=Cat()
    human=Human()

    describe(Dog())
    describe(cat)
    describe(human)

main()