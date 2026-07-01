"""
Dictionary :- A dictionary in Python is a collection that stores data in key-value pairs.
 Each key is unique and is used to find its corresponding value.
"""

"""
Question 1:
Create two dictionaries to store student information and print them.
Also, check the data type of a dictionary using type().
"""

x = {"name": "Rahul", "age": "54", "gender": "Male"}
y = {"name": "Shanu", "age": "38", "gender": "Male"}
print(x)
print(y)
print(type(x))


"""
Create a dictionary containing multiple key-value pairs
and print the dictionary along with its data type.
"""

x = {
    "name": "Rahul",
    "age": "54",
    "gender": "Male",
    "Name": "Aditya",
    "marks": 66,
}

print(x)
print(type(x))


"""
Create a dictionary using both string keys and integer keys.
Print the dictionary and check its data type.
"""

x = {
    "name": "Rahul",
    "age": "54",
    "gender": "Male",
    "Name": "Aditya",
    "marks": 66,
    1: 2,
    2: 3,
}

print(x)
print(type(x))
