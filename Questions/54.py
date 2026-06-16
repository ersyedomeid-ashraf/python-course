"""
Write a program to make your own list. Find the sum of all even numbers present in that list.
"""

my_list = [11, 23, 22, 44, 53, 65, 45, 88, 94, 20, 50]

total = 0

for i in range(0, len(my_list)):

    if my_list[i] % 2 == 0:
        total = total + my_list[i]


print(total)


"""
Write a program to make your own list. Find the sum of all odd numbers present in that list.
"""

my_list = [11, 32, 31, 41, 53, 73, 56, 79, 80, 99, 76, 96, 55]

total = 0

for i in my_list:

    if i % 2 != 0:
        total = total + i

print(total)
