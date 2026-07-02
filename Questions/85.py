"""
Store "name" of a student as Key, "list of 5 marks" of that student as a Value.
Store atleast 5 student names. Print the sum and percentage of all the students.
"""

students_data = {
    "student1": [87, 67, 65, 45, 66],
    "student2": [55, 67, 87, 98, 90],
    "student3": [87, 65, 67, 65, 33],
    "student4": [90, 86, 43, 67, 87],
    "student5": [90, 89, 98, 87, 67],
}


for name, marks in students_data.items():
    total = sum(marks)
    percentage = total / 500 * 100
    print(f" {name} has scored total {total} marks, percentage = {percentage:.2f}")
