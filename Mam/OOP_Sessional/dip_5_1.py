def sum(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiplication(a,b):
    return a*b

def divide(a, b):
    return a//b

def power(a,b):
    return a**b


def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = sum(a, b)
    print(c)
    print(subtract(a,b))
    print(power(a,b))
    print(divide(a, b))

#call a function
main()