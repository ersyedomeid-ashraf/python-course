my_set1 = {43, 45, 44, 43, 45, 56, 76, 82, 46, 76}
my_set2 = {45, 89, 76, 87, 667, 885, 990}

print(my_set1.union(my_set2))
print(my_set1.intersection(my_set2))


# list common example

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8, 9]

c = set(a)
d = set(b)

result = list(c.intersection(d))
print(result)


my_set1 = {44, 73, 56, 67, 78, 89, 29, 45, 66, 78, 75, 43}
my_set2 = {909, 889, 778, 76, 46, 55}

print(my_set1.union(my_set2))
print(my_set1.intersection(my_set2))
