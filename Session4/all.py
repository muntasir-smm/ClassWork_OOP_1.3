'''1. Write a python method called checkNumber() that takes a number and find whether the number is even or odd.'''

def checkNumber(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


'''2. Write a python method called isDivisible() that takes a number as an argument and find whether the number is divisible by 3.'''

def isDivisible(num):
    if num % 3 == 0:
        return "Divisible by 3"
    else:
        return "Not Divisible by 3"


'''3. Write a python method called isLeapYear() that takes a year as an argument and find whether that year is a leap year.'''

def isLeapYear(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"


'''4. Write a python method called WeatherAnalyzer() that takes the temperature as an argument and find the type of temperature.'''

def WeatherAnalyzer(temp):
    if temp < 10:
        return "Cold"
    elif temp < 25:
        return "Moderate"
    else:
        return "Hot"


'''5. Write a python method called isMax()  that takes a list of numbers as an argument and find the maximum number from the list.'''

def isMax(numbers):
    return max(numbers)


'''6. Write a python method called NumType() that takes a number as an argument and find whether the number zero or positive or negative.'''

def NumType(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


'''7. Write a python method called isMin() that takes a list of numbers as an argument and find the minimum number from the list.'''

def isMin(numbers):
    return min(numbers)


'''8. Write a python method called isVowel() that takes a letter as an argument and find whether the letter entered by the user is a vowel or not.'''

def isVowel(letter):
    if letter.lower() in "aeiou":
        return "Vowel"
    else:
        return "Not a Vowel"


'''9. Write a python method called charType() that takes a character as an argument and find whether the character entered by the user is a vowel, or a consonant, or a number.'''

def charType(ch):
    if ch.isdigit():
        return "Number"
    elif ch.lower() in "aeiou":
        return "Vowel"
    elif ch.isalpha():
        return "Consonant"
    else:
        return "Special Character"


'''
10. Write a python method called letterGrade() that takes obtained mark as an argument and determine the letter grade for a mark entered by the user.
You get an A+ if the mark is more than 79, an A if it is between 75 and 79, an A if it is between 70 and 74, a B+ if it is between 65 and 69, a B if it is between 60 and 64, a B if it is between 55 and 59, a C+ if it is between 50 and 54, a C if it is between 45 and 49, a D if it is between 40 and 44, and an F if it is less than 40.
'''
def letterGrade(mark):
    if mark >= 80:
        return "A+"
    elif mark >= 75:
        return "A"
    elif mark >= 70:
        return "A-"
    elif mark >= 65:
        return "B+"
    elif mark >= 60:
        return "B"
    elif mark >= 55:
        return "B-"
    elif mark >= 50:
        return "C+"
    elif mark >= 45:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"


'''11. Write a python method called MoonWeigh() that takes a weight (in kg) of human on earth as an argument and find how much she/he weighs on the moon. (note that your moon weight is 16.5% of your Earth weight)'''

def MoonWeigh(weight):
    return weight * 0.165


'''12. Write a python method called FahToKel() that takes  a temperature in Fahrenheit as an argument and determine the temperature in Kelvin. Formula: Kelvin = (Farh – 32) x 5/9 + 273.15.'''

def FahToKel(fahr):
    kelvin = (fahr - 32) * 5 / 9 + 273.15
    return kelvin



'''13. Write a python method called fiboNum() that takes an integer n as an argument and generates n Fibonacci numbers.'''

def fiboNum(n):
    a, b = 0, 1
    fib = []
    for i in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib


'''14. Write a python method called facNum() that takes an integer n as an argument and generates the factorial of n.'''

def facNum(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


'''15. Write a python method called isPrime() that takes an integer n as an argument and find whether the number is prime or not.'''

def isPrime(n):
    if n <= 1:
        return "Not Prime"

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Not Prime"

    return "Prime"

def add(nums):
    return sum(nums)


print(add([2, 5, 9, 1]))       

# print(checkNumber(8))            # Even
# print(isDivisible(15))           # Divisible by 3
# print(isLeapYear(2024))          # Leap Year
# print(WeatherAnalyzer(30))       # Hot
# print(isMax([2, 5, 9, 1]))       # 9
# print(NumType(-5))               # Negative
# print(isMin([2, 5, 9, 1]))       # 1
# print(isVowel('A'))              # Vowel
# print(charType('7'))             # Number
# print(letterGrade(78))           # A
# print(MoonWeigh(60))             # 9.9
# print(FahToKel(98.6))            # 310.15
# print(fiboNum(10))               # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# print(facNum(5))                 # 120
# print(isPrime(29))               # Prime