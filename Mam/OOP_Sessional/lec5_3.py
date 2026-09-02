#how to generate a list?

city = ["Dhaka", "Chittagong", "Noakhali", "Gaibandha", "Rangpur", "Tangail", "Kushtia", "Kishorganj", "Cumilla", "Barishal", "Faridpur", "Narshingdi", "Laxmipur"]
print(len(city))
#print(sorted(city))
#print(max(city))
city.append("Rajshahi")
print(city)
print(len(city))



city.insert(7, "Pabna")
print(city)

city.insert(3, "Bogra")
city.insert(4, "Khulna")

for i, c in enumerate(city):
    print(i, c)
city.pop() #to delete last element

print("===========divider----------")
for i, c in enumerate(city):
    print(i, c)

del city[7]
print("===========divider----------")
for i, c in enumerate(city):
    print(i, c)

for c in city:
    if 'n' in c:
        print(c)
