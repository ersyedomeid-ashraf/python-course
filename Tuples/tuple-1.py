"""
Tuple - A tuple is an ordered and immutable sequence of elements, where the elements can be of different
data types and are enclosed in parentheses ().
"""

my_tuple = (23, 45, 66, 86, 90)

print(my_tuple)
print(type(my_tuple))


my_tuple = (34, 56, 78, 97, 56)
print(my_tuple[1])


my_tuple = (34, 56, 78, 97, 56)
x = my_tuple.count(56)
print(x)


my_tuple = (34, 56, 78, 34, 97, 56, 34)
x = my_tuple.index(78)
print(x)


my_tuple = (34, 56, 78, 34, 97, 56, 34)
for i in my_tuple:
    print(i)
