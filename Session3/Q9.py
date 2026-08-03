# 9. Write a python program to show summation of n Fibonacci numbers.

n=int(input("Enter a number: "))
f1=0
f2=1
Total=0
print(f"First {n} f2nacci numbers are :")
for i in range(n):
    Total+=f1
    print(f1, end=" ")
    f1,f2=f2,f1+f2
print()
print("Sum= ",Total)