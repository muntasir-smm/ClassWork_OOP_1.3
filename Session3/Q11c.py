'''
11(c). Write a python program to generate the following patterns:

      *
     * *
    * * *
   * * * *
  * * * * *
'''

for i in range(1,6):
  print(" " * (6 - i) + "* " * i)