# 9. Write a python program to find whether a character entered by the user is a vowel, or a consonant, or a number.

char=input("Enter any character: ")

if char.isalpha(): #isalpha() check if it's a letter
    if char.lower() in "aeiou": #lower() convert into lower case
        print(char, "is a vowel.")
    else:
        print(char, "is consonant.")
elif char.isdigit(): #isdigit() check is it is a digit
    print(char, "is a number.")
else:
    print(char, "is special character.")
