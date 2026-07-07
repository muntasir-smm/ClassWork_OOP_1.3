# 9. Write a python program to show summation of n Fibonacci numbers.

n=int(input("Enter a number: "))
sum=0
fibo=1
Total=0
for i in range(n):
    Total+=sum
    sum,fibo=fibo,sum+fibo
print(Total)