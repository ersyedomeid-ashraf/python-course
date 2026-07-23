"""
Write a program to write a function that accepts a string and prints the
frequency of each character in the string.

Example - HELLO

{"H":1, "E":1, "L":2, "O":1}

h occurs 1 times
e occurs 1 times
l occurs 2 times
o occurs 1 times
"""


def charCount(string):

    my_dict = dict()

    for ch in string:

        if ch not in my_dict:
            my_dict[ch] = 1

        else:
            my_dict[ch] += 1

    for k, v in my_dict.items():
        print(f"{k} occurs {v} times")


charCount("HEELLLLLOOOOOOOOOOO")


# Another one


def charCount(string):

    my_dict = dict()

    for ch in string:

        if ch not in my_dict:
            my_dict[ch] = 1

        else:
            my_dict[ch] += 1

    for k, v in my_dict.items():
        print(f"{k} occurs {v} times")


charCount("DHARMENDRA PRATAP ISTIFA DOOOO")
