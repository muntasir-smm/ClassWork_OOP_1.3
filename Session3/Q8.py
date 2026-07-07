# 8. Write a python program to show summation of first 10 Fibonacci numbers.

# n=int(input("Enter a number: "))
sum=0
fibo=1
Total=0
for i in range(10):
    Total+=sum
    # print(sum, end=" ")
    sum,fibo=fibo,sum+fibo
print(Total)