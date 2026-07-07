if __name__ == "__main__":
    celsius = float(input("Enter Celsius temperature: ")) # Take float Celsius temp input from user
    fahrenheit = 9.0 / 5.0 * celsius + 32 # Convert Celsius to Fahrenheit 
    print(fahrenheit) # Print converted Fahrenheit value
    if fahrenheit >= 50 and fahrenheit <= 80:
        print("It's a pretty good day!") # if temp is between 50F and 80F show this msg
    else:
        print("It may be better to stay inside.") # Show this warning if temp is not between 50F and 80F
