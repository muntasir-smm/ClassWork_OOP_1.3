'''
3. Write a python program that takes a string from user and make a pascal case of the string. An example of pascal case: if your string is "This is a test string", the pascal case of the string is "ThisIsATestString". Use PascalCase() method to convert a string pascal case.
'''

# Method to convert string into Pascal Case
def PascalCase(text):
    words = text.split()
    result = ""

    for word in words:
        result += word.capitalize()
        # print(result)

    return result

string = input("Enter a string: ")

print("Pascal Case:", PascalCase(string))