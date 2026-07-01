my_dict = {
    "name": "Rahul",
    "age": "54",
    "gender": "Male",
    "Name": "Aditya",
    "marks": 66,
}

print(my_dict)

# Method 1

# Create a dictionary and update the value of an existing key.

my_dict["age"] = 100
print(my_dict)


# Add a new key-value pair to an existing dictionary and print the updated dictionary.

my_dict["xyz"] = 100
print(my_dict)


# Method 2

# Update multiple values and add a new key to a dictionary using the update() method.

my_dict.update({"marks": 99, "address": "Qatar", "Name": "XYZ"})
print(my_dict)
