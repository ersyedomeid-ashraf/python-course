a = [32, 23, 45, "BMW", True, -65, 89, 98]

pos = a.index(89)  # Get element position
print(pos)


a = [23, 2, 4, 3, 56, 76, 7, 6, 8, 90]
a.sort()  # It arrange in ascending order
print(a)


a = [3, 7, 64, 4, 32, 56, 67, 89, 90]
a.reverse()  # It reverse the list
print(a)


"""
Write a program to print the list in descending order 
"""

a = [10, 43, 23, 45, 33, 22, 34, 87, 65, 90, 98, 45]

a.sort()
a.reverse()
print(a)


a = [33, 22, 43, 89, 70, 89, 98, 77, 43, 21, 25]

a.sort(reverse=True)
print(a)


a = [23, 43, 54, 65, -98, -81, "Virtus", "Slavia", 34.5]

a.append(["BMW", "Code", "Python", 200])  # Add single element at end of list
print(a)


a = [23, 43, 54, 65, -98, -81, "Virtus", "Slavia", 34.5]

a.extend(["BMW", "Code", "Python", 200])  # Add multiple elements at end of list
print(a)


a = [23, 43, 54, 65, -98, -81, 43, "Slavia", 43, 34.5]

r = a.count(43)
print(r)


a = [33, 22, 43, 89, 70, 89, 98, 77, 43, 21, 25]

a.clear()
print(a)
