"""
Write a program to make your own list. Print the sum of all the elements present in the list.
"""

my_list = [21, 32, 43, 54, 65, 76, 87, 98, 202]

# Iteration by index

total = 0
for i in range(0, len(my_list)):
    total = total + my_list[i]

print(total)


# Iteration by value

my_list = [21, 32, 43, 54, 65, 76, 87, 98, 202]

total = 0

for i in my_list:
    total = total + i

print(total)
