# 3. Write a python program to show average of n numbers.
n=int(input("Enter a number: "))
# sum=0
# for i in range(1,n+1):
#     sum+=i
sum=n*(n+1)/2
avg=sum/n;
print("Average = ",avg)