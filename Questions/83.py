"""
Write a program to sum all the items in dictionary .
"""

marks = {
    "physics": 76,
    "chemistry": 86,
    "computer": 77,
    "english": 93,
    "Maths": 37,
}

total = 0

for v in marks.values():
    total = total + v

print(total)

# or we'll write in short also

print(sum(list(marks.values())))
