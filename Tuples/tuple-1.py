"""
Tuple - A tuple is an ordered and immutable sequence of elements, where the elements can be of different
data types and are enclosed in parentheses ().
"""

# Write a Python program to create a tuple and display its type.

my_tuple = (23, 45, 66, 86, 90)

print(my_tuple)
print(type(my_tuple))


# Write a Python program to access an element from a tuple using its index.

my_tuple = (34, 56, 78, 97, 56)
print(my_tuple[1])


# Write a Python program to count the number of occurrences of a specific element in a tuple.

my_tuple = (34, 56, 78, 97, 56)
x = my_tuple.count(56)
print(x)


# Write a Python program to find the index of a given element in a tuple.

my_tuple = (34, 56, 78, 34, 97, 56, 34)
x = my_tuple.index(78)
print(x)


# Write a Python program to traverse and display all elements of a tuple using a for loop.

my_tuple = (34, 56, 78, 34, 97, 56, 34)
for i in my_tuple:
    print(i)
