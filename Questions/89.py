"""
Write a program given two lists a,b. Check if two lists have atleast one element common in them.
"""

list1 = [3, 4, 5, 6, 55, 7, "laila", 77, 6, 2, 3, 4, 5, 55, 66, 7, 764]
list2 = [3, 4, "laila", 55, 3, 4, 77, 8, 7]

set1 = set(list1)
set2 = set(list2)

print(set1.intersection(set2))


# also we'll write this

print(set2 & set2)  # here (&) means intersection
