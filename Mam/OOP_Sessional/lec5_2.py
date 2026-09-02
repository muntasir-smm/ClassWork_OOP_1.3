import math

def add(a, b):
    return a+b

def sub(a, b):
    pass

def mul(a, b):
    pass

def division(a, b):
    pass

def power(a, b):
    return a**b

def logf(a, b):
    logtwo = math.log2(a)
    logten = math.log10(b)
    return logtwo, logten

def sqrt(a):
    return a**0.5
    #return math.sqrt(a)



def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    sum = add(a, b)
    print(sum)
    x, y = logf(a, b)
    print(x,y)
    s = sqrt(a)
    print(s)

main()  #main function is called here