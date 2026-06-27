"""
Write a program to ask a string from user. Count how many alphabets are
there in that string.
"""

my_string = "abcd1234"

count = 0

for ch in my_string:
    if ch.isalpha():
        count = count + 1

print(count)


# Count alphabets using ASCII values.

my_string = "abcd1234"

count = 0

for ch in my_string:
    ascii = ord(ch)

    if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
        count += 1

print(count)
