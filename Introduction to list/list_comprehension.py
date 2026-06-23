"""
list Comprehension - A list comprehension is a concise way to create a list in Python using a single line of code.
"""

# Without list Comprehension

my_list = []
for i in range(1, 21):
    my_list.append(i)

print(my_list)


# With list Comprehension


my_list = [i for i in range(1, 31)]

print(my_list)


"""
i=1 ODD
i=2 EVEN
[ODD,EVEN,ODD,EVEN]
"""


my_list = ["EVEN" if i % 2 == 0 else "ODD" for i in range(1, 11)]
print(my_list)


# [2,4,6,8,.......26,28,30]

my_list = [i for i in range(1, 31) if i % 2 == 0]
print(my_list)
