n = int(input("Enter number of lines: "))


# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end=" ")
    
#     for j in range(i):
#         print("*", end=" ")
    
#     print()

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
