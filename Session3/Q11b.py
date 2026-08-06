'''
11(b). Write a python program to generate the following patterns:

* * * * *
* * * *
* * *
* *
*
'''

for i in range(5,0, -1):
    for j in range(i):
        print("*", end=" ")
    print()