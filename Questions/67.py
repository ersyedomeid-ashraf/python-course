"""
Write a python code to find the occurrence of each element in a list
and print the element with the highest occurrence
"""

my_list = [2, 4, 6, "code", 4, "python", 2, "code", 4, 1, 3, "billa"]
result = []

for num in my_list:
    if num not in result:
        result.append(num)

highest_occ_element = 0
highest_occurrence = 0


for num in result:
    c = my_list.count(num)  # count occurrence of current element
    print(f"{num} occurrs {c} times")
    if c > highest_occurrence:
        highest_occurrence = c
        highest_occ_element = num

print(f"Highest occurrence element = {highest_occ_element}")


# Another one

my_list = [2, 4, 8, 5, "laila", 4, 3, 4, "code", "BMW", 6, 9]
result = []

for num in my_list:
    if num not in result:
        result.append(num)

highest_occ_element = 0
highest_occurrence = 0


for num in my_list:
    c = my_list.count(num)  # count occurrence of current element
    print(f"{num} occurrs {c} times")
    if c > highest_occurrence:
        highest_occurrence = c
        highest_occ_element = num


print(f"Highest occurrence element = {highest_occ_element}")
