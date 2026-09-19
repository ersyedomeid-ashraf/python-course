"""
Write a program to input two numbers from the user and divide the first number by the second number.
Handle the ZeroDivisionError exception if the second number is zero.
"""

try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:

    print("Cannot divide by zero.")


"""
Write a Python program to accept an integer from the user and display its square. 
Handle the ValueError exception if the user enters an invalid value.
"""

try:

    num = int(input("Enter a number: "))

    print("Square:", num**2)

except ValueError:

    print("Invalid input. Please enter an integer.")


"""
Write a Python program to create a list containing five elements. Accept an index from the user and display 
the element at that index. Handle the IndexError exception for an invalid index.
"""

try:

    my_list = [87, 67, 99, 62, 22]

    index = int(input("Enter index: "))
    print("Element:", my_list[index])

except IndexError:

    print("Invalid Index")
