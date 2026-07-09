"""
Write a program to create 3 set of your own, find the union of three sets.
"""

list1 = [45, 3, 4, 4, 5, 56, "laila", 67, 76, 5, 4, 3, 4556, "tinaa", 654, 767, 678]
list2 = [4, 5, 654, 45, 789, 78, 899, 87, 667, 66, 55, "laila"]
list3 = [5, 4, 3, "laila", "tina", 45, 4556, 654, 767]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

print(set1 | set2 | set3)
