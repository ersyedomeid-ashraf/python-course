"""
Write a program to ask a number from user. Print all the number from 1 to that number.
"""


num = int(input("Enter a number = "))

i = 1 
while i <= num :
    print(i)
    
    i = i + 1 


# if we take in single line 


num = int(input("Enter a number = "))

i = 1 
while i <= num :
    print(i,end = " ")

    i = i + 1 