# 5. Write a python program to find factorial of first 10 numbers.
fact=1
for i in range(1,11):
    fact*=i
    print(f"Factorial of {i} is = {fact}")