# 4. Write a python program to find the type of temperature entered by the user.

n=float(input("Enter a temperature in celsius: "))

if n>40:
    print("Extremely hot. Don't go outside.")
elif n>35:
    print("Very hot. Try to stay inside.")
elif n>25:
    print("Hot weather. Take umbrella.")
elif n>17:
    print("Very nice weather.")
elif n>8:
    print("Cold weather, take jacket.")
elif n>=0:
    print("Very cold, Turn on heater.")
else:
    print("Ice cold. Stay inside")
