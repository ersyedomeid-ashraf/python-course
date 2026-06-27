"""
Write a program to ask a string from user. Convert all the alphabets to uppercase.
"""

my_string = "abcdedf1234ABCD"

result = my_string.upper()
print(result)

# Convert all the alphabets to uppercase using with ASCII value.

my_string = "abcdedf1234ABCD"
result = ""

for ch in my_string:
    ascii = ord(ch)
    if ascii >= 97 and ascii <= 122:
        new_ascii = ascii - 32
        char = chr(new_ascii)
        result += char

    else:
        result += ch

print(result)
