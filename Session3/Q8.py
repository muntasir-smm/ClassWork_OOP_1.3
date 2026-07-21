# 8. Write a python program to show summation of first 10 bnacci numbers.

# n=int(input("Enter a number: "))
a=0
b=1
Total=0
for i in range(5):
    Total+=a
    # print(a, end=" ")
    a,b=b,a+b
print(Total)