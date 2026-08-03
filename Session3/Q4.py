# 4. Write a python program  to show all Odd and Even numbers in the range given by the user.

a,b = map(int,input("Enter 2 numbers (a<b): ").split())

print("Odd numbers are: ")
for i in range(a,b+1):
    if(i%2!=0):
        print(i, end=" ")

print("\nEven numbers are: ")
for i in range(a,b+1):
    if(i%2==0):
        print(i, end=" ")