"""
Write a program to store name as key, and 5 marks in a List as a value in dictionary. Store details
of at least 5 students. Print the name of the student who got highest marks.
"""

student_data = {
    "Satish": [67, 76, 87, 98, 90],
    "Dilip": [89, 98, 76, 78, 56],
    "Rajesh": [89, 76, 67, 90, 78],
    "Munna": [76, 89, 90, 66, 65],
    "Umesh": [98, 78, 67, 99, 90],
}

highest_marks = 0
highest_student_name = ""

for name, marks in student_data.items():
    total = sum(marks)

    if total > highest_marks:
        highest_marks = total
        highest_student_name = name


print(highest_student_name)
print(highest_marks)
