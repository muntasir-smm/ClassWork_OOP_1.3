# 6. Write a python program to find whether a number zero or positive or negative.

n=int(input("Enter a number: "))

if n>0:
    print(n,"is a positive number.")
elif n<0:
    print(n,"is Negative number.")
else:
    print("This is Zero.")