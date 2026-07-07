'''11. Write a python program to generate the following patterns:
(a)
*
* *
* * *
* * * *
* * * * *'''


for i in range(1, 5+1):
    for j in range(i):
        print("*", end=" ")
    print()