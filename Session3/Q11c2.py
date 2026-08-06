'''
11(c2). Write a python program to generate the following patterns:

* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''

n=int(input("Enter number of row: "))

for i in range(n,0,-1):
  print(" " * (n - i) + "* " * i)
