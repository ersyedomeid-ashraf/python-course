"""
Write a program to ask the user for a number. Then, from a list of numbers, remove all the numbers
that can divisible by the number the user entered.
"""

numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]  # List of numbers

n = int(input("Enter a number: "))  # Ask the user for a number

new_list = []  # Create a new list

for num in numbers:  # Add only numbers that are not divisible by n
    if num % n != 0:
        new_list.append(num)

print("Original list:", numbers)
print("Updated list:", new_list)
