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
