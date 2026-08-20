from abc import ABC, abstractmethod
class Human(ABC):
    @abstractmethod
    def doAction(self):
        pass
    @property
    @abstractmethod
    def ethnicity(self):
        pass
class Nationality(Human):
    def __init__(self, ethnicity):
        self.__ethnicity = ethnicity
    def doAction(self):
        print("I can read and write Bangla")
    @property
    def ethnicity(self):
        return self.__ethnicity
    @ethnicity.setter
    def ethnicity(self, value):
        self.__ethnicity = value

sumaiya = Nationality("Bangladeshi")
print("The nationality is " + sumaiya.ethnicity)
sumaiya.ethnicity = "Kolkata"
print(f"{sumaiya.doAction()} The nationality is now {sumaiya.ethnicity}")