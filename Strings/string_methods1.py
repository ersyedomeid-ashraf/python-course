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
