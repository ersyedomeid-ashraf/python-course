"""
WAP to create a set containing integer numbers. Separate the even and odd numbers
into two different sets and display both sets.
"""

numbers = {10, 15, 22, 31, 40, 55, 62, 73}

even = set()
odd = set()

for n in numbers:
    if n % 2 == 0:
        even.add(n)
    else:
        odd.add(n)

print("Even numbers:", even)
print("Odd numbers:", odd)


"""
WAP to input a sentence from the user and create a set of unique words present in the sentence.
Display the set and the total number of unique words.
"""


sentence = input("Enter a sentence: ")

words = sentence.split()
unique_words = set(words)

print("Unique words:", unique_words)
print("Total unique words:", len(unique_words))
