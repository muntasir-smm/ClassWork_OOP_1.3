# 7. Write a python program to generate n Fibonacci numbers.

n=int(input("Enter a number: "))
sum=0
fibo=1
print(f"First {n} Fibonacci numbers are: ")
for i in range(n):
    print(sum, end=" ")
    sum,fibo=fibo,sum+fibo
    # next=sum+fibo
    # sum=fibo
    # fibo=next