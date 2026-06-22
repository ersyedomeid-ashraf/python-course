"""
Write a program to split a given list into two halves.
"""

my_list = [1, 2, 3, 4, 5, 6]


mid = len(my_list) // 2

first_half = my_list[:mid]
second_half = my_list[mid:]

print("First half:", first_half)
print("Second half:", second_half)


# Another one

my_list = [11, 12, 13, 14, 15, 16, 17, 18, 19]


mid = len(my_list) // 2

first_half = my_list[:mid]
second_half = my_list[mid:]

print("First half:", first_half)
print("Second half:", second_half)
