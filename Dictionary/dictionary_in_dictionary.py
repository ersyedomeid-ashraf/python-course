"""
Create a Python dictionary to store details of multiple students. Each student should have a roll number,
gender, and marks in Physics, Chemistry, and Maths. Iterate through the dictionary and print
 each student's name, total marks, and gender.
"""

student_data = {
    "Zehra": {
        "roll_number": 67,
        "gender": "female",
        "physics": 78,
        "chemistry": 90,
        "maths": 90,
    },
    "Neha": {
        "roll_number": 22,
        "gender": "female",
        "physics": 58,
        "chemistry": 64,
        "maths": 76,
    },
    "Sheikh": {
        "roll_number": 33,
        "gender": "female",
        "physics": 89,
        "chemistry": 60,
        "maths": 98,
    },
}

for name, details in student_data.items():
    total = details["physics"] + details["chemistry"] + details["maths"]
    gender = details["gender"]
    print(f"{name} -> {total}, gender = {gender}")


"""
Employee Salary Create a nested dictionary named employee_data that stores details of 3 employees: 
-employee_id
- department 
- basic_salary 
- bonus
"""

employee_data = {
    "Rahul": {
        "employee_id": 101,
        "department": "IT",
        "basic_salary": 50000,
        "bonus": 8000,
    },
    "Priya": {
        "employee_id": 102,
        "department": "HR",
        "basic_salary": 45000,
        "bonus": 5000,
    },
    "Aman": {
        "employee_id": 103,
        "department": "Finance",
        "basic_salary": 55000,
        "bonus": 7000,
    },
}

for name, details in employee_data.items():
    total_salary = details["basic_salary"] + details["bonus"]
    department = details["department"]

    print(f"{name} -> Department: {department}, Total Salary: {total_salary}")


"""
Write a Python program to store student details in a nested dictionary and calculate
the total marks of each student from a list of marks.
"""
student_data = {
    "Sakshiiiiiii": {
        "roll_number": 67,
        "gender": "female",
        "marks": [90, 98, 87, 86, 89],
    },
    "Nehaaaaaaaa": {
        "roll_number": 22,
        "gender": "female",
        "marks": [87, 78, 69, 97, 90],
    },
    "Javeriyaaa": {
        "roll_number": 33,
        "gender": "female",
        "marks": [80, 87, 98, 77, 76],
    },
}

for name, details in student_data.items():
    total = sum(details["marks"])
    print(f"{name} has scored {total}marks")
