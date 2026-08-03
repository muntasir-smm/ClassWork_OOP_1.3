'''
11(a). Write a python program to generate the following patterns:

*
* *
* * *
* * * *
* * * * *
'''


for i in range(1, 5+1):
    for j in range(i):
        print("*", end=" ")
    print()