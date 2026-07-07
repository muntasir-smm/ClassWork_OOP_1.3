# How to generate a list?

city=["Dhaka", "Gaibandha", "Rangpur","Rajshahi","Noakhali"]
print(len(city))

# for c in city:
#     print(c)

city.append("Mars") #added at the last

# print(city)
print(len(city))

# for i, c in enumerate(city):
#     print(f"Index:{i} City: {c} ")

# city.insert(3, "Pabna")
city[3:4] = ["Pabna","Khulna", "Bogura", "Natore"]
print(city)
del city[8]
# city.insert(3, "Khulna","Bogura","Natore")
# print(city)
for i, c in enumerate(city):
    print(f"Index:{i} City: {c} ")

print(":::::::Print city with the letter n in it::::::::::")
for c in city:
    if 'n' in c:
        print(c)