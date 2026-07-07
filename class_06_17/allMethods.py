# ==============================
# 1. Sample Data
# ==============================
mixed_data = [319,"10", "42.5", "Python", "  ", "hello", "Munna"]
raw_text = "python programming 2026!"

print("\n:::::::: 1. Built-in Functions ::::::::")

# len() - Get the total number of items in our list
print(f"Total items in list: {len(mixed_data)}")

# int() and float() - Convert string representations into actual numbers
first_num = int(mixed_data[0])
second_num = float(mixed_data[1])

# round() - Round the floating-point number
rounded_num = round(second_num)
print(f"Original float: {second_num} -> Rounded: {rounded_num}")

# max() and min() - Find the highest and lowest numeric elements
print(f"Maximum: {max(first_num, rounded_num)}")
print(f"Minimum: {min(first_num, rounded_num)}")

# range() - Generate an iterable sequence to loop through a specific count
print("Range loop:")
for i in range(3):
    print(f"  i = {i}")

# enumerate() - Loop through our list while tracking both index and element automatically
print("\nEnumerate loop:")
for index, element in enumerate(mixed_data):
    # type() - Check the data type of the current element
    print(f"  Index {index}: {element} (Type: {type(element)})") #type(element).__name__


# ==============================
# 2. String Methods
# ==============================
print("\n:::::::: 2. String Methods ::::::::")

# capitalize() - Capitalize the very first letter of the sentence
print("Capitalize:", raw_text.capitalize())

# upper() and lower() - Transform case variations completely
print("Upper:", raw_text.upper())
print("Lower:", raw_text.lower())

# replace() - Swap out substring tokens
print("Replace:", raw_text.replace("2026", "world"))

# ==============================
# 3. String Checks (is methods)
# ==============================
print("\n--- 3. String Checks ---")

word1 = "LeetCode"
word2 = "12345"
word3 = "Python3"
word4 = "SHOUTING"

print(f"{word1} isalpha: {word1.isalpha()}")
print(f"{word2} isdigit: {word2.isdigit()}")
print(f"{word3} isalnum: {word3.isalnum()}")
print(f"{word4} isupper: {word4.isupper()}")
print(f"{word1} islower: {word1.islower()}")