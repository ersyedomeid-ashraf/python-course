"""
Write a program to create a list and prompt the user for an 'old number' followed by a 'new number' if the 'old number'
exists in the list, replace it with the 'new number' provided by the user.
"""

my_list = [22, 34, 65, 76, 89, 99, 100, 120]

old = int(input("Enter old number = "))
new = int(input("Enter new number = "))

for i in range(0, len(my_list)):

    if my_list[i] == old:
        my_list[i] = new

print(my_list)


my_list = [78, 54, 65, 76, 90, 190, 456]

old = int(input("Enter old number = "))
new = int(input("Enter new number = "))

for i in range(0, len(my_list)):

    if my_list[i] == old:
        my_list[i] = new

print(my_list)
