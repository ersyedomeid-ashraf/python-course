"""
Write a program to print the last digit of a number. 
Example -> Input = 12345 Output = 5.
"""

num = int(input("Enter a number = "))

last_digit = num % 10 
print(f"The last digit of {num} is {last_digit}")
