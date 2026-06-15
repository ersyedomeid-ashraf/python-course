"""
Write a program to make your own list. Count the number of even numbers present in that list.
"""

my_list = [32, 43, 54, 67, 87, 97, 34, 44, 66, 88, 90, 20]

count = 0

for i in range(0, len(my_list)):
    if i % 2 == 0:
        count = count + my_list[i]


print(count)


"""
Count the number of odd numbers present in that list.
"""

my_list = [32, 43, 54, 67, 87, 97, 34, 44, 66, 88, 90, 20]

count = 0

for i in range(0, len(my_list)):
    if i % 2 != 0:
        count = count + my_list[i]


print(count)
