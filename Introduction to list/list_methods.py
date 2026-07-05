# Mutable / Immutable Data Types

"""
 Mutable -> Object whose vallues can be changed after creation.
example - list, doct, set

Immutable -> objects whose values cannot be chnaged after creation.
example - int, float, str, tuple
"""

a = [56, 62, 72, 81, -90]
print(a)

a.append(200)  # append() is used to add a single elements to a list
a.append("you can write whatever you want")
print(a)


a.insert(3, "Python")
# insert() is used to add an element at a specific position in a list
a.insert(2, "Code")
print(a)


a[0] = 220  # update() changes existing values or adds new key-values in dictionary
a[-3] = 118
print(a)


a.pop(1)  # Remove by index (pop() removes elements by index and returns it)
a.remove(72)
# Remove by value (remove() deletes the first matching value from the list)


del a[2]  # del is used to delete variables or list/dictionary elements
a.clear()  # clear() removes all elements from list or dictionary
print(a)


a = [56, 62, 72, 81, -90, 88, 98]
print(a)

a.append(200)  # append() is used to add a single elements to a list
a.append("you can write whatever you want")
print(a)
