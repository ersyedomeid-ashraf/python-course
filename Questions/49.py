"""
Write a program to make your own list. Print all the odd numbers present in the list.
"""

my_list = [31, 557, 87, 54, 33, 99, 87, 67, 80, 83, 45]

# Iteration by index

for i in range(0, len(my_list)):
    if my_list[i] % 2 != 0:
        print(my_list[i], end=" ")


# Iteration by value

for i in my_list:
    if i % 2 != 0:
        print(i, end=" ")
