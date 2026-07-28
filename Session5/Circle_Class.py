'''
Write Python programs for creating following classes and their objects:
2. Circle Class
'''
import math

class Circle:
    def __init__(self,radious,area,perimeter):
        self.radious=radious
        self.area=area
        self.perimeter=perimeter
    

def main():
    PI=math.pi
    r=float(input("Enter the radiousof the circle:"))
    a=PI*r**2
    p=2*PI*r
    circle1=Circle(r,a,p)
    print(f"radious: {circle1.radious}\narea: {circle1.area:.3f}\nperimeter: {circle1.perimeter:.3f}")

main()