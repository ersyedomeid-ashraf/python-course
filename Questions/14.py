"""
Write a program to check if the number is divisible by 2 and 3 but not 8.
"""

num = int(input("Enter a number = "))

if num%2 == 0 and num%3 == 0 and num%8 != 0 :
    print("Yes it is divisible by 2, 3 but not 8 ")

else :
    print("No")
    