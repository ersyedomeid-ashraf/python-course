my_set = set()

print(my_set)
print(type(my_set))
my_set.add(120)
my_set.add(340)

# methods example

my_set = {4, 5, 6, 7, 8}

print(my_set)

my_set.add(230)

print(my_set)


my_set.remove(230)
print(my_set)


# membership operator

my_set = {1, 2, 2, 3, 4, 56, 7, 8}

num = int(input("Enter a number = "))

# In the easiest way
if num in my_set:
    print("Yes")

else:
    print("No")


# In other way

found = False
for i in my_set:
    if i == num:
        found = True


if found:
    print("Yes")

else:
    print("No")
