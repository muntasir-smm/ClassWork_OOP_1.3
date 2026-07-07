if __name__ == "__main__":
    age = 0  # Initialize age variable with value 0
    country = input("Enter your country of residence: ")  # Take country input from user
    if (country == "Bangladesh"):  # Check if the user is from Bangladesh
        age = int(input("How old are you? "))  # Ask for age and convert input to integer
        if (age >= 18):
            print("You are allowed to vote") # Print message if age is 18 or older
        else:
            print("You are not allowed to vote") # Print message If age is less than 18
    else:
        print("Voting laws unknown")  # If country is not Bangladesh show this msg