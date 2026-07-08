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
