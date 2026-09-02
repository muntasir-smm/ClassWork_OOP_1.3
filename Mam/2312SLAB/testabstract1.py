from abc import ABC, abstractmethod
class Polygon(ABC):
# abstract method
    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):
# overriding abstract method
    def noofsides(self):
        print("I have 3 sides")
class Pentagon(Polygon):
# overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
class Hexagon(Polygon):
# overriding abstract method
    def noofsides(self):
        print("I have 6 sides")
class Quadrilateral(Polygon):
# overriding abstract method
    def noofsides(self):
        print("I have 4 sides")

triangle = Triangle()
triangle.noofsides()
pentagon = Pentagon()
pentagon.noofsides()
hexagon = Hexagon()
hexagon.noofsides()
quadrilateral = Quadrilateral()
quadrilateral.noofsides()
