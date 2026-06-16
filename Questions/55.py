"""
Write a program to make  your own list. Find the sum of all numbers divisible by 3 and 4 in that list.
"""

my_list = [12, 24, 33, 36, 45, 60, 64, 54, 84, 600]

total = 0

for i in my_list:

    if i % 3 == 0 and i % 4 == 0:
        total = total + i


print(total)


"""
Write a program to make your own list. Print how many positive and negative numbers are here. 
"""

my_list = [21, 23, -11, -50, 45, -58, 0, -55, -90, -45, 66, -89]

positive = 0
negative = 0

for i in range(0, len(my_list)):
    if my_list[i] > 0:
        positive = positive + 1
    elif my_list[i] < 0:
        negative = negative + 1


print("Positive numbers:", positive)
print("Negative numbers:", negative)
