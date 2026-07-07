if __name__=="__main__":
    secretNum=5
    userGuess=int(input("Enter a number between 1 and 10: "))

    while (1< userGuess <10):        
        if userGuess==secretNum:
            print(str(userGuess ) + " is the secret number")
            break
        else:
            print(str(userGuess) + " isn't the secret number")
        userGuess=int(input("Not between 1 and 10. Try again!"))
