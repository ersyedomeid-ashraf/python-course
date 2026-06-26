"""
Palindrome - A palindrome is a word, number, or string that reads the same forward and backward.
"""

my_string = input("Enter a string = ")

if my_string == my_string[::-1]:
    print("It is a palindrome")

else:
    print("It is not a palindrome")
