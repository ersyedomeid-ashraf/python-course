# Sets: Store unique values
# - Unordered
# - Mutable (can be modified)
# - Do not support indexing

my_set = {2, 1, 34, 5, 64, 2, 1, "laila", 88.4, 3, 88.4, 2}

print(my_set)


for i in my_set:
    print(i)


# Type conversion example

a = [1, 2, 3, 1, 2, 3, 1, 2, 2, 2, 3, 3, 3, 78, 98, 44]

print(a)
b = set(a)
print(b)
c = list(b)
print(c)
