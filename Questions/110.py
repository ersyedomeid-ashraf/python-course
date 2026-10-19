"""
Write a program to find the longest word in a sentence.
"""

sentence = "I'm trying my best to learn everything as quickly as possible"

words = sentence.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)


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
