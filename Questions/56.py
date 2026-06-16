"""
Write a program to make your own list. Print the largerst number present in that list.
"""

my_list = [3, 4, 6, 100, 887, 337, 10]

largest = 0

for i in range(0, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]


print(largest)


"""
Write a program to make your own list. Print the largerst number present in that list.
"""


my_list = [-33, -54, -32, -69, -22, -11, -10, -69]

largest = my_list[0]

for i in my_list:

    if i > largest:
        largest = i

print(largest)
