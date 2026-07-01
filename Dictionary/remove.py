# Create a dictionary and delete a specific key-value pair using the del keyword.

my_dict = {
    "name": "Rahul",
    "age": "54",
    "gender": "Male",
    "Name": "Aditya",
    "marks": 66,
}

print(my_dict)

del my_dict["gender"]
print(my_dict)


# Create a dictionary and remove a specific key-value pair using the pop() method.

my_dict = {
    "name": "Rahul",
    "age": "54",
    "gender": "Male",
    "Name": "Aditya",
    "marks": 66,
}

print(my_dict)

my_dict.pop("name")
my_dict.popitem()
print(my_dict)


# Create a dictionary and remove the last key-value pair using the popitem() method.

my_dict = {
    "name": "Rahul",
    "age": "54",
    "gender": "Male",
    "Name": "Aditya",
    "marks": 66,
}

print(my_dict)


my_dict.popitem()
print(my_dict)
