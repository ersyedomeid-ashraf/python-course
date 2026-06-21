"""
Write a program to make a list. Then ask a number from user. If number exist in that list
then print the position of the element else print -1.
"""

my_list = [5, 1, "python", 55.43, 66, 5, 1, 5, "code", 1, 1, "python"]

value = int(input("Enter a value = "))

if value in my_list:

    index = my_list.index(value)
    print(f"Index = {index}")
else:
    print(-1)
