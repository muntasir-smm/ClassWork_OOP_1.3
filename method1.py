'''
1. Write a python program that calculates the area of a rectangle, triangle, and circle. Use the following methods for calculating area- areaRectangle(), areaTriangle(), and areaCircle(). You have to ask user to choose on of the three shapes (i.e., rectangle, triangle, or circle) then ask him/her to give input according to chosen shape. For example if the user choses circle, you have to ask him/her to give input for a radius. Then calculate the area of chosen shape and display it.
'''


import math

# Method to calculate area of rectangle
def areaRectangle(length, width):
    return length * width

# Method to calculate area of triangle
def areaTriangle(base, height):
    return 0.5 * base * height

# Method to calculate area of circle
def areaCircle(radius):
    return math.pi * radius * radius


print("Choose a shape:")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    x = float(input("Enter length: "))
    y = float(input("Enter width: "))
    print(f"Area of Rectangle = {areaRectangle(x, y):.2f}")

elif choice == 2:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of Triangle =", areaTriangle(base, height))

elif choice == 3:
    radius = float(input("Enter radius: "))
    print("Area of Circle =", areaCircle(radius))

else:
    print("Invalid Choice!")