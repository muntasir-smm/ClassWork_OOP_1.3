'''11. Write a python program to generate the following patterns:
(c)
         *
       * *
      * * *
    * * * *
   * * * * *'''

for i in range(1,6):
    print(" " * (6 - i) + "* " * i)