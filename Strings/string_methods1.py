"""
Title, Capitalized, upper, lower, swapcase,
isupper, islower, isalpha, isalnum, isspace
"""

a = "syed humaid ashraf"
x = a.title()
print(x)


a = "syed humaid ashraf"
x = a.capitalize()
print(x)


a = "syed humaid ashraf"
x = a.upper()
print(x)


a = "syed humaid ashraf"
x = a.lower()
print(x)


a = "syed humaid ashraf"
x = a.swapcase()
print(x)


a = "syed humaid ashraf"
x = a.isupper()
print(x)


a = "syed humaid ashraf"
x = a.islower()
print(x)


a = "BareillyUttarPradesh"
x = a.isalpha()
print(x)


a = "Syed1humaid2ashraf"
x = a.isalnum()
print(x)


a = "223454398700"
x = a.isdigit()
print(x)


a = "syed humaid ashraf"
x = a.isspace()
print(x)


a = "surya1234"

if a.isdigit():
    a = int(a)
    print(a, type(a))

else:
    print("Cannot be converted into integer")


# Split and Join

# Split - split() is a string method that breaks a string into a list of smaller parts using a separator.


a = "this is a python program"
words = a.split("-")
print((words))


# if we check how many words ar there
a = "this-is-a-python-program"
words = a.split("-")
print(len(words))


# Join - join() is a string method that combines the elements of a list into a single string using a separator.

my_list = ["abc", "lalla", "python", "programming"]

my_string = " ".join(my_list)
print(my_string)
print(type, (my_string))


# What if i did

my_list = ["abc", "lalla", "python", "programming"]

my_string = "-".join(my_list)
print(my_string)
print(type, (my_string))


# What if i want integer value also

my_list = ["abc", "lalla", "python", "programming", 72, 81, 64]

my_string = " ".join(str(i) for i in (my_list))
print(my_string)
print(type, (my_string))


# Count, Startswith, Endswith, Index,
# Find, Replace, Strip


my_string = "khwaish adhuri ho toh rabb kitna yaad aata hai "

c = my_string.count("k")
print(c)


c = my_string.count("a")
print(c)


c = my_string.count("i")
print(c)


# Startswith string method

my_string = "hello python program"

c = my_string.startswith("hello")
print(c)

c = my_string.startswith("python")
print(c)


# Endswith string method

my_string = "the python programming"

c = my_string.endswith("programming")
print(c)

c = my_string.endswith("the")
print(c)
