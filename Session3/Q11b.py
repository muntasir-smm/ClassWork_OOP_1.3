'''11. Write a python program to generate the following patterns:
(b)
* * * * *
* * * *
* * *
* *
*'''

for i in range(5,1, -1):
    for j in range(i):
        print("*", end=" ")
    print()