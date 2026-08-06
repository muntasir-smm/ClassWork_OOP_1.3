'''
11(c). Write a python program to generate the following patterns:

      *
     * *
    * * *
   * * * *
  * * * * *
'''

n=int(input("Enter number of row: "))

for i in range(1,n+1):
  print(" " * (n - i) + "* " * i)