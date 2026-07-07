def myFun(x,y):
    avg=(x+y)/2
    return avg

def main():
    x=float(input("Enter a number: "))
    y=float(input("Enter a number: "))

    print(f"Average = {myFun(x,y)}")

if __name__=="__main__":
    main()