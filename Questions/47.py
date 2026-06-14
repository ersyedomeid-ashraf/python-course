"""
Write a program to make your own list. Print the list in reverse
"""

my_list = [34, 76, 88, "Jaguar", 96, 54, 34, 45, 577, 800, 9888, 766, 544]

# 0 to 5
# 5 to 0
# length = 6

for i in range(len(my_list) - 1, -1, -1):

    print(my_list[i], end=" ")


# One more porgram

my_list = [78, 65, 76, 87, "Mustang GT", "Porche", 67, 65, 6554, 677]

for i in range(len(my_list)):
    print(my_list[i], end=" ")
