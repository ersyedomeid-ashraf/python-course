"""
Write a program to create a function that takes a number
and prints whether it is positive, negative or zero.
"""


def check_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")


num = int(input("Enter a number = "))

check_number(num)


"""
Write a program to create a function that takes a number
and returns its cube.
"""


def cube(num):
    return num * num * num


num = int(input("Enter a number = "))

result = cube(num)

print(f"Cube = {result}")
