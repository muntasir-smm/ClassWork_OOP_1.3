# 10. Write a Python program to determine the letter grade for a mark entered by the user. You get an A+ if the mark is more than 79, an A if it is between 75 and 79, an A if it is between 70 and 74, a B+ if it is between 65 and 69, a B if it is between 60 and 64, a B if it is between 55 and 59, a C+ if it is between 50 and 54,  a C if it is between 45 and 49, a D if it is between 40 and 44, and an F if it is less than 40.

mark=float(input("Enter you marks: "))

if mark>79:
    print("You get an A+ ")
elif 75<=mark:
    print("You get an A ")
elif 70<=mark:
    print("You get an A- ")
elif 65<=mark:
    print("You get a B+ ")
elif 60<=mark:
    print("You get a B ")
elif 55<=mark:
    print("You get a B- ")
elif 50<=mark:
    print("You get a C+ ")
elif 45<=mark:
    print("You get a C ")
elif 40<=mark:
    print("You get a D ")
else:
    print("You get F")
