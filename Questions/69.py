"""
Write a python code to find the second largest element in a list
without sorting.
"""

my_list = [54, 32, 17, 67, 43, 11, 87, 44, 54, 32]


largest = float("-inf")
second_largest = float("-inf")

for num in my_list:

    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num < largest:
        second_largest = num

print(second_largest)


# Another one

my_list = [45, 32, 24, 56, 98, 76, 57, 89, 90, 223, 46, 78, 97, 43]

largest = float("-inf")
second_largest = float("-inf")

for num in my_list:

    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num < largest:
        second_largest = num

print(second_largest)
