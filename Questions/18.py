"""
Write a program Ask 4 numbers from the user. Make sure all the numbers entered by user 
are different. Print which number is the samllest. 
"""

num1 = int(input("Enter a number 1  = "))
num2 = int(input("Enter a number 2 = "))
num3 = int(input("Enter a number 3 = "))
num4 = int(input("Enter a number 4 = "))

if num1<num2 and num1<num3 and num1<num4 : 
    print("num1 is the smallest")

elif num2<num1 and num2<num3 and num2<num4 :
    print("num2 is the smallest")

elif num3<num1 and num3<num2 and num3<num4 :
    print("num3 is the smallest")

else :
    print("num4 is the smallest")
 