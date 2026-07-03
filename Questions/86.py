"""
Write a program to stroe marks of 5 different subjects in a dictionary. Ask subject name as an input
from the user. Print the marks of that subject entered by user. If subject does not
 exist, print "Invalid".
"""

subject_marks_dict = {
    "Maths": 98,
    "Science": 90,
    "Computer": 89,
    "English": 94,
    "History": 75,
}

subject_name = input("Enter subject name = ")

if subject_name in subject_marks_dict:
    print(subject_marks_dict[subject_name])

else:
    print("Invalid")
