'''student={
    "id": [202610546, 202610423, 202610144],
    "name": ["Abul", "Kabul", "Habul"],
    "cgpa" : [3.8, 4.0, 2.4]
}
print(student["id"][0])
print(student["name"][0])
print(student["cgpa"][0])'''

numbers = {x: x**2 for x in range(10)}

print(numbers)
for key in numbers:
    print(key, numbers[key])

w = "This is an example text"

for e in w.split():
    print(e.capitalize(), end="")

numList = [3, 5 1, 43, 56]

