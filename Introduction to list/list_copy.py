a = [56, 68, 100, 5, "Billa", True, 55.556, "Heera"]
b = a.copy()  # Create a seperate copy of the list in different memory

print(a)
print(id(a))  # Show unique memory address of object

print(b)
print(id(b))  # Show unique memory address of object


a[2] = 0  # Modify value at given index

print(a)
print(b)
