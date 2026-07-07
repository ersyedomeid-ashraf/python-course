"""
Write a Python program to add a new element to a tuple by converting it into a list.
"""

my_tuple = (44, 66, 88, 22, 32, 90, 76)


my_list = list(my_tuple)  # Convert tuple into list
my_list.append(120)  # Add a new element to the list

my_tuple = tuple(my_list)  # Convert list back to tuple
print(my_tuple)


"""
Write a Python program to insert a new element at a specific position in a tuple.
"""

my_tuple = (10, 20, 30, 40, 50)

my_list = list(my_tuple)  # Convert tuple into list

my_list.insert(2, 25)  # Insert a new element at index 2

my_tuple = tuple(my_list)  # Convert list back to tuple


print(my_tuple)


"""
Write a Python program to add multiple elements to a tuple.
"""

my_tuple = (1, 2, 3)

my_list = list(my_tuple)

my_list.extend([4, 5, 6])  # Add multiple elements

my_tuple = tuple(my_list)  # Convert list back to tuple


print(my_tuple)


# WAP to sort the elements of a tuple in ascending order and display the sorted tuple.


t = (45, 12, 89, 23, 67, 5)

sorted_tuple = tuple(sorted(t))

print("Original Tuple:", t)
print("Sorted Tuple:", sorted_tuple)
