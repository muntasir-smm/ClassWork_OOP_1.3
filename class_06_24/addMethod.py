def add(a,b):
    return a+b

def sub(a,b):
    return a-b

if __name__=="__main__":
    x=float(input("Enter 1st number: "))
    y=float(input("Enter 2nd number: "))

    print("Sum of ",x," and ",y," = ", add(x,y))
    print("Sub of ",x," and ",y," = ", sub(x,y))