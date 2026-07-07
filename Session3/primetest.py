# Write a python program to test n is prime or not.

import math

n = int(input("Enter a number: "))

if n < 2:
    print("Not Prime")
else:
    is_prime = True
    sq = int(math.sqrt(n))

    for i in range(2, sq + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")