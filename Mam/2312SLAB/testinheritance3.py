'''implement a class hierarchy to model pets in a pet store, 
starting with a base class Pet that has attributes name (string) and price (float), 
and a method get_description() that returns a string with the name and price (e.g., "Buddy, $500"). 
Define two subclasses: Dog and Cat. 
The Dog class should add attributes breed (string) and weight (float, kg), 
and override get_description() to include these (e.g., "Buddy, $500, Labrador, 30.5kg"). 

The Cat class should add attributes color (string) and is_indoor (boolean), and 
override get_description() to include these (e.g., "Whiskers, $300, Black, Indoor"). 

Inheritance ensures that Dog and Cat inherit name and price from Pet while adding specific traits. 

Test: Create a Dog object with name "Buddy", price 500.0, breed "Labrador", and weight 30.5, and 
a Cat object with name "Whiskers", price 300.0, color "Black", and is_indoor as True. 
Print their descriptions using get_description().
'''
class Pet:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_description(self):
        return f"Name: {self.name}, Price: {self.price:.2f} Taka"

class Cat(Pet):
    def __init__(self, name, price, color, in_door):
        #super().__init__(name, price)
        Pet.__init__(self, name, price)
        self.color = color
        self.in_door = in_door
    def get_description(self):
        if self.in_door == True:
            cat_lives = "Indoor"
        else:
            cat_lives = "outdoor"
        return f"Name: {self.name}, Price: {self.price:.2f} Taka, Color: {self.color}, {cat_lives}"
    
cat = Cat("Kitty", 508.56, "White", False)
print(cat.get_description())