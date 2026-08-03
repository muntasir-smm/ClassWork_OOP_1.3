# 8. Write a python program to show summation of first 10 Fibonacci numbers.

# n=int(input("Enter a number: "))
f1=0
f2=1
Total=0
print("First 10 Fibonacci numbers are :")
for i in range(10):
    Total+=f1
    print(f1, end=" ")
    f1,f2=f2,f1+f2
print()
print("Sum= ",Total)