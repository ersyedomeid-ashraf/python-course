"""
Write a porgram that reverse each word in a sentence while maintaining the word order.
For example, "Hello" should become "olleH"
"""

my_string = "python is good"
words = my_string.split()

result = " ".join(i[::-1] for i in words)
print(result)


# Another one program

my_string = "my brother is my hero"
words = my_string.split()

result = " ".join(i[::-1] for i in words)
print(result)
