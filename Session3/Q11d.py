'''11. Write a python program to generate the following patterns:
(d)
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

(e)
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1'''

for i in range(1, 5+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()