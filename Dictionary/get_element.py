"""
Create a dictionary and access its values using square brackets ([]).
"""

my_dict = {
    "name": "Rahul",
    "age": "54",
    "gender": "Male",
    "Name": "Aditya",
    "marks": 66,
}

# To get a value
print(my_dict["name"])
print(my_dict["age"])

"""
Access a dictionary value using the get() method and print the returned value.
"""
r = my_dict.get("name")
print(r)
print(type(r))


"""
Write a Python program to ask the user for a dictionary key and display its value.
"""

k = input("Enter a key")
result = my_dict.get(k)

if result is not None:
    print(result)

else:
    print("Key does not exist")
