# 6. Write a python program to find factorial of n numbers.

n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact*=i
    print(f"Factorial of {i} is = {fact}")