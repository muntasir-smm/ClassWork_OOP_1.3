# 3. Write a python program to find whether a year is a leap year.

n=int(input("Enter a year: "))

if ((n%4==0 and n%100!=0)or (n%400==0)):
    print(n, "is Leap year.")
else:
    print(n, "is not Leap year.")
