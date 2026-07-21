'''
2. Write a python program that takes a string from user and capitalize the first letter of each word of that string. Use a method called MakeCapital() to capitalize the first letter of each word.
'''

# Method to capitalize each word
def MakeCapital(text):
    return text.title()

string = input("Enter a string: ")

print("Capitalized String:", MakeCapital(string))