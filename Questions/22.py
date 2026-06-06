"""
Write a program to ask start number and end number from the user. 
Print all the numbers from start to end using while loop.
"""

start = int(input("Enter a number = "))
end = int(input("Enter a number = "))

i = start 
while i <= end :
    print(i, end = " ")

    i = i + 1 