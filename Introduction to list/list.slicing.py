a = [23, 12, 34, 55, 78, 90, 87, 765]

b = a[0:4]
print(b)


a = [23, 45, 67, 765, 54, 56, 900, 998, 98, 765, 43]

b = a[3:6]
print(b)


a = [98, 765, 56, 778, 899, 876, 54, 34, 567, 89, 900, 345]

b = a[::-1]
print(b)


"""
Write a slicing expression to get the first 4 elements.
"""
a = [43, 55, 78, 77, 89, 90, 34, 67]

b = a[:4]
print(b)


"""
Write a slicing expression to get the elements from 78 to 34.
"""

a = [43, 55, 78, 77, 89, 90, 34, 67]

b = a[2:6]
print(b)


"""
Write a slicing expression to get every second element.
"""

a = [87, 96, 66, 54, 78, 81, 43, 89]

b = a[::2]
print(b)


"""
Write a slicing expression to get all elements at even indices.
"""

a = [54, 66, 53, 72, 81, 90, 44, 66, 78, 100]

b = a[::2]
print(b)


"""
Write a slicing expression to get all elements at odd indices.
"""

a = [54, 66, 53, 72, 81, 90, 44, 66, 78, 100]

b = a[1::2]
print(b)
