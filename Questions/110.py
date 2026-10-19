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
