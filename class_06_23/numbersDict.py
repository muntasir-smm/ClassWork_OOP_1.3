numbers={
    "Square":{x:x**2 for x in range(1,11)},
    "Cube":{x:x**3 for x in range(1,11)}
    }

# print(numbers["Cube"])

for key in numbers:
    print(f"{key}:")
    print(*numbers[key].items(), sep="\n")
    print()