if __name__ == "__main__":
    celsius = float(input("Enter Celsius temperature: ")) # Take float Celsius temp input from user
    fahrenheit = 9.0 / 5.0 * celsius + 32 # Convert Celsius to Fahrenheit 
    print(fahrenheit) # Print converted Fahrenheit value
    if fahrenheit >= 70:
        print("the temperature is pleasant and suggest a picnic") # Shows warning if temp is more than or equal 70F, even if more than 90F
    elif fahrenheit >= 80:
        print("it is warm, but there is no extreme heat") # dont show this warning if temp more than or equal 80F, shows warning of 70F condition
    elif fahrenheit >= 90:
        print("heat warning")# dont show this warning if temp more than or equal 90F, shows warning of 70F condition
    else:
        print("a suggestion to take a jacket") # Shows warning if temp is less than 70F
