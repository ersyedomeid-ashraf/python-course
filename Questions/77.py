"""
Write a program to reverse the order of words.
"""

my_string = "Python is good"

words = my_string.split()
print(words)

words = words[::-1]

result = " ".join(i for i in words)
print(result)


# Another one program

my_string = "10 rupee ki pepsi tera bhai sexy"

words = my_string.split()
print(words)

words.reverse()

result = " ".join(i for i in words)
print(result)
