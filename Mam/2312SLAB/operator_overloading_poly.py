class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, obj):
        return Vector(self.x + obj.x, self.y + obj.y)
    def __sub__(self, obj):
        return Vector(self.x - obj.x, self.y - obj.y)
    def __mul__(self, num):
        return Vector(self.x * num, self.y * num)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
# Usage
v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(v1 + v2) # Vector(7, 10)
print(v2 - v1) # Vector(3, 4)
print(v1 * 3) # Vector(6, 9)