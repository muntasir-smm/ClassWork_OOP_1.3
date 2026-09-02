marks = int(input("Enter your marks: "))

if marks>=80:
    print("A+")
elif marks>=75:
    print("A")
elif marks>=70:
    print("A-")
#65-B+, 60-B, 55-B-, 50-C+, 45-C, 41-D,
else:
    print("F")