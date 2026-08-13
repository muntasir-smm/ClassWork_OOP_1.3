age=int(input("Enter your age: "))

def howCs(cs):
    if cs>=700:
        return 3
    elif cs>=600:
        return 2
    else:
        return 1
    
if age<18:
    print("You do not qualify for a loan due to age.")
else:
    income=int(input("Enter your income: "))
    cs=int(input("Enter your Credit Score (between 300 and 850): "))
    
    if (income>=100000) & (howCs(cs)==3):
        print("Premium loan")
    elif (income>=50000) & (howCs(cs)>=2):
        print("Standard loan")
    elif (income<50000) & (howCs(cs)==2):
        print("Basic loan")
    else:
        print("Your income is too low for a loan.")

