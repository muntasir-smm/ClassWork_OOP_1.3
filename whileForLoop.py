n=int(input("Enter a  number: "))
m=n
print("While loop: ")

while m>0:
    if m%2==0:
        print(m, end=' ')
    m=m-1

print()
print("For loop: ")

for i in range(1,n):
    if i%2==0:
        print(i, end=' ')
