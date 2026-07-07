# 10. Write a python program to generate n prime numbers.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
x=int(input("Enter a number "))
count=0
i=2
while(count<x):
    if is_prime(i):
        print(i)
        count+=1
    i+=1
        