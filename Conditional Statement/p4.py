"""
Ask Five numbers from user.
Calculate percentage and print it.

91-100 -> A grade 
81-90  -> B grade 
71-80  -> C grade 
61-70 ->  D grade 
1-60  ->  FAIL 
Invalid 
"""

maths = int(input("Enter marks in maths = "))
science = int(input("Enter marks in science = "))
hindi = int(input("Enter marks in hindi = "))
english = int(input("Enter marks in english = "))
geography = int(input("Enter marks in geography = "))

total = maths+science+hindi+english+geography

percentage = (total/500)*100
print(f"percentage scored = {percentage}%")

if percentage >= 91 and percentage <= 100 :
    print("A grade")

elif percentage >= 81 and percentage <= 90 :
    print("B grade")

elif percentage >= 71 and percentage <= 80 :
    print("C grade")

elif percentage >= 61 and percentage <= 70 :
    print("D grade")

elif percentage >= 1 and percentage <= 60 :
    print("FAIl")
     
else:
    print("Invalid Percentage") 
