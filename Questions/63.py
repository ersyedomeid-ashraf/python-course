"""
Write a program to make your own list. And remove all the duplicates elements from that list.
"""

my_list = [1, 3, 5, "Python", 44.32, "Code", 1, 2, 5, "Python", 5, 44.32]
result = []

for num in my_list:

    if num not in result:
        result.append(num)

print(result)
