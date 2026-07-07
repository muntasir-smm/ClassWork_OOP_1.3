name="Alim"
lenth=len(name)

# for letter in name:
#     print(letter+"-",end="")
#     print(name[2])

for i in range(lenth):
    print(name[i],end="")
    if not i==3:
        print("-",end="")