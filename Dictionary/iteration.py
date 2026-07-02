# Write a Python program to print all the keys of a dictionary.

my_dict = {
    "name": "lulla",
    "age": 25,
    "gender": "male",
}

for k in my_dict.keys():
    print(k)


# Write a Python program to print all the values of a dictionary.

my_dict = {
    "name": "lulla",
    "age": 25,
    "gender": "male",
}

for k in my_dict.values():
    print(k)


# Write a Python program to calculate and print the total marks stored in a dictionary.

my_dict = {
    "history": 67,
    "conputer": 88,
    "science": 90,
    "english": 99,
}


total_marks = 0
for v in my_dict.values():
    total_marks = total_marks + v

print(total_marks)
