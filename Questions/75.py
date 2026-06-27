"""
Write a program to ask a string from user. Count the number of uppercase and lowercase
character in that string.
"""

my_string = "abcde12345ABCD"

lower_count = 0
upper_count = 0

for ch in my_string:
    if ch.isupper():
        upper_count += 1

    elif ch.islower():
        lower_count += 1

print(upper_count)
print(lower_count)


# Count the number of uppercase and lowercase alphabet characters using ASCII values.

my_string = "abcd12345ABCD"

lower_count = 0
upper_count = 0

for ch in my_string:
    ascii = ord(ch)
    if ascii >= 65 and ascii <= 90:
        upper_count += 1

    elif ascii >= 97 and ascii <= 122:
        lower_count += 1

print(upper_count)
print(lower_count)
