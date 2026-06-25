"""
String - String is a sequence of character enclosed within single quotes (' ') or double quotes (" ").
A string cannot be changed after it is created.
"""

a = "Python Code"

print(a, type(a))

print(a[2])
print(a[3])
print(a[-4])

# Iterate string

my_string = "Python Code"
# By index, By value

for index in range(0, len(my_string)):  # by index
    print(my_string[index])


for ch in my_string:  # by value
    print(ch)


for i in range(len(my_string) - 1, -1, -1):
    print(my_string[i])


"""
Write a program to reverse a string.
"""

s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

print("Reversed String:", reverse)


"""
Write a program to print all characters with their positions.
"""

s = input("Enter a string: ")

for i in range(len(s)):
    print(i, s[i])
