"""
Write a program to input two numbers from the user and divide the first number by the second number.
Handle the ZeroDivisionError exception if the second number is zero.
"""

try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:

    print("Cannot divide by zero.")
