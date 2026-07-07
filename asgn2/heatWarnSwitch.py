if __name__ == "__main__":    
    fahrenheit = float(input("Enter the temperature as fahrenheit : "))  #take temp input from user and convert into float
    conditions = int(fahrenheit/10) #divide the fahrenheit by 10 to determine the 10s place
    print("It is in the " + str(conditions) + "0's.") # shows temp range group
    match conditions: # decide advice based on 10s place
        case 10:
            print("Stay inside" ) # shows this if temperature between 100 to 109
        case 9:
            print("Be careful due to heat" ) # shows this if temperature between 90 to 99
        case 8:
            print("It is hot, but not extreme" ) # shows this if temperature between 80 to 89
        case 7:
            print("Pack a picnic" ) # shows this if temperature between 70 to 79
        case _:
            print("Take a jacket" ) #default msg if temp below 70 or above 109