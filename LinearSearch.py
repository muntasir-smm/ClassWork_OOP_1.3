numbers = list(map(float, input("Enter numbers: ").split()))
# print(list(enumerate(numbers)))
key = float(input("Enter number to search: "))

for position, num in enumerate(numbers):
    if num == key:
        print(f"Found at position {position +1}")
        break
else:
    print("Not Found")