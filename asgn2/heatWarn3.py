if __name__ == "__main__":
    celsius = float(input("Enter Celsius temperature: ")) # Take float Celsius temp input from user
    fahrenheit = 9.0 / 5.0 * celsius + 32 # Convert Celsius to Fahrenheit 
    print(fahrenheit) # Print converted Fahrenheit value
    if (fahrenheit >= 90):
        print("heat warning!") # Shows this warning if temp is more than or equal 90 F
    else:
        print("there is no extreme heat") # Show this if temp is less than 90F
