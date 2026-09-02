n = int(input("Enter a number: "))
m = n
print("while loop")
while m>0:
    if m%2 == 0:
        print(m)
    m=m-1
print()

print("for loop")

for i in range(1,n):
    if i%2==0:
        print(i, end=' ')
print()