"""
Write a program to ask a number from user. Print all the number from 1 to that number.
"""

num = int(input("Enter a number = "))

i = 1
while i <= num:
    print(i)

    i = i + 1


# if we take in single line


num = int(input("Enter a number = "))

i = 1
while i <= num:
    print(i, end=" ")

    i = i + 1


"""
Write a porgram to convert two lists into a dictionary. Make two list on your own of
same length, and convert them to dictionary.
"""

list1 = ["python", "programming", "good", "bye"]
list2 = [54, "wow", "lalla", 72]

result = {}

for i in range(0, len(list1)):
    result[list1[i]] = list2[i]

print(result)
