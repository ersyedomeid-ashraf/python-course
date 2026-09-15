"""
WAP to create a set containing integer numbers. Separate the even and odd numbers
into two different sets and display both sets.
"""

numbers = {10, 15, 22, 31, 40, 55, 62, 73}

even = set()
odd = set()

for n in numbers:
    if n % 2 == 0:
        even.add(n)
    else:
        odd.add(n)

print("Even numbers:", even)
print("Odd numbers:", odd)
