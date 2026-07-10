"""
Write a program to check if two given sets have no elements in common.
"""

set1 = {45, 67, 45, "Aaruhiii", 68, 90, 87}
set2 = {76, 57, 45, 67, "Aaruhiii", 90, -65, 1}

result = set1.intersection(set2)

if len(result) == 0:
    print("Both sets have nothing in common")

else:
    print("Sets have something in common")
    print(result)


# Another one

set1 = {34, 45, 67, 87, "Naina", 90, -98}
set2 = {54, 56, 76, 78, "Sunaina", 89, -43, 2}

result = set1.intersection(set2)

if len(result) == 0:
    print("Both sets have nothing in common")

else:
    print("Sets have something in common")
    print(result)


"""
Write a program to check if two given sets have no elements in common.
"""

set1 = {45, 67, 45, "Aaruhiii", 68, 90, "Kallan", 87}
set2 = {76, "Kallan", 57, 45, 67, "Aaruhiii", 90, -65, 1}

result = set1.intersection(set2)

if len(result) == 0:
    print("Both sets have nothing in common")

else:
    print("Sets have something in common")
    print(result)
