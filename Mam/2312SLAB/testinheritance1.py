class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def printall(self): #method overriedes
        print(self.name)
        print(self.age)
        print(self.gender)

class Employee(Person): 
    def __init__(self, name, age, gender, salary):
        Person.__init__(self, name, age, gender)
        #super().__init__(name, age, gender)
        self.salary = salary
    def printall(self): #method overriedes
        print(self.name)
        print(self.age)
        print(self.gender)        
        print(self.salary)         

#emp1=Employee("Nahid", 20, "Male", 20252)
#emp1.printall()
class Manager:
    def __init__(self, name, id, location):
        self.name = name
        self.id = id
        self.location = location
    def printall(self): #method overriedes
        print(self.name)
        print(self.id)
        print(self.location)
class CEO(Employee, Manager): #mulitple inheritance
    def __init__(self, name, age, gender, salary, id, location):
        Employee.__init__(self, name, age, gender, salary)
        Manager.__init__(self, name, id, location)

    def printall(self):
        print(self.name)
        print(self.age)
        print(self.gender)        
        print(self.salary) 
        print(self.id)
        print(self.location)

ceo1 = CEO("Nahid", 20, "male", 254100, 25, "Bangladesh")
ceo1.printall()