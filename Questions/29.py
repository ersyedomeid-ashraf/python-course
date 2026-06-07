"""
Write a program to ask a start number and end number from user. print all the numbers 
from start to end. 
"""


start = int(input("Enter a start number = "))
end = int(input("Enter a end number = "))

for i in range (start, end +1) :
    print(i, end = " ")