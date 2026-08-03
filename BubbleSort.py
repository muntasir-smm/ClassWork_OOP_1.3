num = list(map(int, input("Enter numbers: ").split()))

n = len(num)

for i in range(n):
    for j in range(n - i - 1):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]

print("Sorted List:", *num)