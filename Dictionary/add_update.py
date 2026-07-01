my_dict = {
    "name": "Rahul",
    "age": "54",
    "gender": "Male",
    "Name": "Aditya",
    "marks": 66,
}

print(my_dict)

# Method 1

my_dict["age"] = 100
print(my_dict)


my_dict["xyz"] = 100
print(my_dict)


# Method 2

my_dict.update({"marks": 99, "address": "Qatar", "Name": "XYZ"})
print(my_dict)
