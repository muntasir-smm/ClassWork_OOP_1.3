cl=["Austrslia","Bangladesh","China","Denmark","Egypt","Finland","Ghana","Honduras","India","Japan","Kosovo","Lotvia","Malta","Nepal","Oman","Poland","Quatar","Russia","Somalia","Turky","Boliva","Brasil"]

l=input("Enter any latter to find country: ")
# l=l.upper()

count=0

for i in range(len(cl)):
    if l==cl[i][0]:
        print(cl[i])
        count+=1
if count==0:
    print("No country is found.")
