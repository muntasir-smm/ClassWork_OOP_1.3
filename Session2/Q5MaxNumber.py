# a=int(input("Enter 1st number: "))
# b=int(input("Enter 2nd number: "))
# c=int(input("Enter 3rd number: "))
# taking multiple inputs at a time
# x, y, z = (input("Values: ").split()) #this is str

a,b,c = map(int,input("Enter 3 numbers: ").split()) # this is integer
print("Maximum ",max(a,b,c))
