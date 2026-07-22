"""
Write a program to write a function that takes three number as a parameter
and prints the largest among them.
"""


def largest(num1, num2, num3):

    if num1 > num2 and num1 > num3:
        print("num1")
        print(f"{num1} is the largest")

    elif num2 > num1 and num2 > num3:
        print(num2)
        print(f"{num2} is the largest")

    else:
        print("num3")
        print(f"{num3} is the largest")


largest(233, 465, 421)


# Another one


def largest(num1, num2, num3):

    if num1 > num2 and num1 > num3:
        print("num1")
        print(f"{num1} is the largest")

    elif num2 > num1 and num2 > num3:
        print(num2)
        print(f"{num2} is the largest")

    else:
        print("num3")
        print(f"{num3} is the largest")


largest(9898, 8989, 9988)
