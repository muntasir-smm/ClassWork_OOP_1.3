def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    return x / y

def remainder(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    return x % y


def calculate(a, b):
    print(f"Sum        = {add(a, b)}")
    print(f"Difference = {subtract(a, b)}")
    print(f"Product    = {multiply(a, b)}")
    print(f"Division   = {divide(a, b):.4f}")
    print(f"Remainder  = {remainder(a, b)}")


if __name__ == "__main__":
    a = float(input("Enter x: "))
    b = float(input("Enter y: "))
    calculate(a, b)