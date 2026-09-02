def myFunc(x, y):
    avg = (x+y)/2
    return avg

def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    r = myFunc(x,y)
    print(r)

     
if __name__ == "__main__":
    main()
    
