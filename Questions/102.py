"""
Write a program to write a function that takes a string and prints whether
it is a palindrome.
"""


def check_palindrome(string):

    if string == string[::-1]:
        print("It is a palindrome")

    else:
        print("It is not a palindrome")


check_palindrome("mom")
check_palindrome("anaa")
check_palindrome("madam")
