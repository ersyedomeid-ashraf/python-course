"""
Write a program to make your own list. Print all the elements present at even index position.
"""

my_list = [21, 43, 45, 32, "Hurray", 89, 76, "Done", "Done"]


# Iteration by index

for i in range(0, len(my_list)):
    if i % 2 == 0:
        print(my_list[i], end=" ")


"""
Write a program to make your own list. Print all the elements present at even index position.
"""


my_list = [21, 43, "Smart", 32, "Hurray", 89, 76, "Done", "Done"]


# Iteration by index

for i in range(0, len(my_list)):
    if i % 2 != 0:
        print(my_list[i], end=" ")
