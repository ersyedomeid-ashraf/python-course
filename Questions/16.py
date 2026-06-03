"""
Write a program to check if the last digit of a number is divisible by 5 or not. 
"""

num = int(input("enter a number = "))

last_digit = num % 10

if last_digit == 0 or last_digit== 5 :
    print("Yes, it is divisible by 5")

else :
    print("No, it is not divisible by 5")

