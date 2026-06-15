"""
Write a program to make your own list. Print all the even numbers present in the list.
"""

my_list = [54, 65, 34, 34, 56, 67, 87, 85, 90, 98]


# Iteration by index
for i in range(0, len(my_list)):
    if i % 2 == 0:
        print(my_list[i], end=" ")


# Iteration by value

for i in my_list:
    if i % 2 == 0:
        print(i, end=" ")
