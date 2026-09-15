"""
WAP to input a string from the user and count the number of uppercase
and lowercase characters present in it.
"""

text = input("Enter a string: ")

upper = 0
lower = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase characters:", upper)
print("Lowercase characters:", lower)


"""
WAP to input a string and a character from the user. Count how many 
times the given character occurs in the string.
"""


text = input("Enter a string: ")
ch = input("Enter a character: ")

count = 0

for x in text:
    if x == ch:
        count += 1

print("Character occurs", count, "times")
