"""Membership_Operators :-

Membership operators (`in` and `not in`) are used to check whether
an element exists in a collection or not.

"""

a = [23, 22, 45, 66, "Skills", 55.43, "True", 90]

print(23 in a)
print("false" not in a)
print(3 in a)

# Ask a number from user
# Print yes if number exists in list else print no

num = int(input("Enter a number = "))
if num in a:
    print("Yes")

else:
    print("No")


# Another way to check element presence using count()

num = int(input("Enter a number = "))
if a.count(num) > 0:
    print("Yes")
else:
    print("No")
