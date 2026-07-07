if __name__ == "__main__":
    celsius = float(input("Enter Celsius temperature: ")) # Take float Celsius temp input from user
    fahrenheit = 9.0 / 5.0 * celsius + 32 # Convert Celsius to Fahrenheit 
    print(fahrenheit) # Print converted Fahrenheit value
    if fahrenheit >= 90:
        print("heat warning") # Shows warning if temp is more than or equal 90 F
    elif fahrenheit >= 80:
        print("it is warm, but there is no extreme heat") # Shows warning if temp is more than or equal 80F and less than 90F
    elif fahrenheit >= 70:
        print("the temperature is pleasant and suggest a picnic") # Shows warning if temp is more than or equal 70F and less than 80F
    else:
        print("a suggestion to take a jacket") # Shows warning if temp is less than 70F
