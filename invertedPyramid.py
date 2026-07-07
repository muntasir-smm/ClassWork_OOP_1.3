n = int(input("Enter number of lines: "))

for i in range(n+1):
    print(" " * i + "* " * ((n - i)))