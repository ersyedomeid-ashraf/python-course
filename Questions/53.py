"""
Write a program to make your own list. Count how many numbers are divisible by 2 and 5 in that list.
"""

my_list = [10, 23, 40, 88, 76, 55, 98, 60, 95, 34, 54, 100]

count = 0

for i in range(0, len(my_list)):

    if my_list[i] % 2 == 0 and my_list[i] % 5 == 0:
        count = count + 1

print(count)


"""
Write a program to make your own list. Count how many numbers are divisible by 4 and 6 in that list.
"""

my_list = [12, 24, 36, 57, 66, 98, 200, 400, 600, 1200]

count = 0

for i in my_list:
    if i % 4 == 0 and i % 6 == 0:
        count = count + 1


print(count)
