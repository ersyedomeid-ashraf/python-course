"""
Write a program to ask a number from user. print the multiplication table to that number.
"""

num = int(input("Enter a number = "))

for i in range(1, 11) :
    print(f"{num} * {i} = {num * i}") 

