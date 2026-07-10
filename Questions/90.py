"""
Write a program to find common elements in three lists using sets.
"""

list1 = [45, 3, 4, 4, 5, 56, "laila", 67, 76, 5, 4, 3, 4556, "tinaa", 654, 767, 678]
list2 = [4, 5, 654, 45, 789, 78, 899, 87, 667, 66, 55, "laila"]
list3 = [5, 4, 3, "laila", "tina", 45, 4556, 654, 767]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

x = set1.intersection(set2)
result = x.intersection(set3)

print(result)


# in short way we'll write

print(set(list1) & set(list2) & set(list3))


"""
Write a program to find common elements in three lists using sets.
"""

list1 = [
    45,
    3,
    4,
    4,
    5,
    56,
    "laila",
    67,
    76,
    "Kaaalu",
    4,
    3,
    4556,
    "tinaa",
    654,
    767,
    678,
]
list2 = [4, 5, 654, 45, 789, 78, "Kaaalu", 899, 87, 667, 66, 55, "laila"]
list3 = [5, 4, 3, "laila", "tina", 45, 4556, "Kaaalu", 654, 767]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

x = set1.intersection(set2)
result = x.intersection(set3)

print(result)
