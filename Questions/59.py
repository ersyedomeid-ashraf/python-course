"""
Write a program to remove all the even numbers from the lists.
"""

a = [45, 65, 12, 32, 99, 87]
b = []

for i in a:

    if i % 2 == 1:
        b.append(i)


print(b)


# now we will try to how we remove from this a=[45,65,12,32,99,87,44,67,35,29]

a = [45, 65, 12, 32, 99, 87, 44, 67, 35, 29]

for i in a[:]:

    if i % 2 == 0:
        a.remove(i)

print(a)
