if __name__ == "__main__":
    celsius = float(input("Enter Celsius temperature: ")) # Take float Celsius temp input from user
    fahrenheit = 9.0 / 5.0 * celsius + 32 # Convert Celsius to Fahrenheit 
    print(fahrenheit) # Print converted Fahrenheit value
    if 20 >= fahrenheit or fahrenheit >= 90:
        print("Extreme weather warning!") # Shows warning if temp is less than or equal to 20F, or more than or equal 90F; ie Extreme cold or hot weather
