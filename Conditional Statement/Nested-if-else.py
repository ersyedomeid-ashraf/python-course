"""
Write a program to check whether a given number is positive, negative or equal to zero. 
"""
# This is method 1 :
num = int(input("Enter a number = "))

if num >= 0 :
    if num > 0 :
        print("Postive")
    
    else :
        print("Equal to zero ")

else :
    print("Negative")


# This is method 2 :

if num > 0 :
    print("Positive")

else :   # <=0
    if num == 0 :
        print("Equal to zero")

    else :
        print("Negative") 
           
  