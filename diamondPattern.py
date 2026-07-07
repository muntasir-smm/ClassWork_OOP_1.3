n = int(input("Enter number of lines: "))

for i in range(n + 1):
    print(" " * (n - i) + "* " * i)

for i in range(n):
    print(" " * i + " *" * ((n - i) - 1))