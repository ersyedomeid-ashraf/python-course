"""
Write a program to check if the number is ODD, EVEN or EQUAL to Zero 
"""

num = int(input("Enter a number = "))    #In Python 0%2 = 0 

if num == 0 :
    print("It is equal to zero")

elif num%2 == 1 :
    print("ODD")

else :
    print("EVEN")
    