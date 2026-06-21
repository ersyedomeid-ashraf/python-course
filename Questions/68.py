"""
Write a program that has two lists and amke a new list that contains
only the common elements between them without duplicate.
"""

my_list1 = [1, 2, 3, 4, 5, 6, 7, 8]
my_list2 = [6, 7, 8, 9, 10]

result = []

for num in my_list1:
    if num in my_list2:
        if num not in result:
            result.append(num)

print(result)


# Another one

my_list1 = [11, 12, 5, 14, 6, 15, 16, 17, 18]
my_list2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

result = []

for num in my_list1:
    if num in my_list2:
        if num not in result:
            result.append(num)

print(result)
