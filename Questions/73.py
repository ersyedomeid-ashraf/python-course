"""
Write a program that swaps first and last elements of a given list.
"""

my_list = [10, 20, 30, 40, 50]

n = len(my_list)

my_list[0], my_list[n - 1] = my_list[n - 1], my_list[0]

print(my_list)


# Another one

my_list = [20, 25, 40, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

n = len(my_list)

my_list[0], my_list[n - 1] = my_list[n - 1], my_list[0]

print(my_list)
