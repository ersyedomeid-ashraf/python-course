"""
Ask a string from user. Display the dictionary where each key is a character and value
is the frequency of that character that comes in that string.
"""

my_string = input("Enter a string = ")

freq = {}

for ch in my_string:
    if ch in freq:
        freq[ch] += 1

    else:
        freq[ch] = 1


print(freq)
