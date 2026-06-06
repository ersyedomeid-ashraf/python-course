"""
Write a program to ask a number (N) from user. Print all the numbers from N to 1. 
"""


num = int(input("Enter a number = "))

i = num 
while i >= 1 :
    print(i, end = " ")

    i = i - 1 