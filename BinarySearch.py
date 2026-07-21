numbers = list(map(int, input("Enter numbers: ").split()))
numbers.sort()  # Sort the list to work

key = int(input("Enter number: "))

low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == key:
        found = True
        break
    elif numbers[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Found")
else:
    print("Not Found")