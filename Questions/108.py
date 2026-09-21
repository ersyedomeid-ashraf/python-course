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


"""
Write a Python program to accept two numbers and perform division. Handle both ValueError and 
ZeroDivisionError using separate except clauses.
"""

try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Result:", num1 / num2)

except ValueError:

    print("Please enter valid numbers.")

except ZeroDivisionError:

    print("You cannot divide by zero.")


"""
Write a Python program to accept two numbers and perform division. If no exception occurs, 
display the result and a success message using the else clause.
"""

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print("Result:", result)
    print("Division successful.")


"""
Write a Python program to accept a number from the user and calculate its square. Handle invalid input using except, 
display a success message using else, and display a completion message using finally.
"""

try:
    num = int(input("Enter a number: "))

    print("Square:", num**2)

except ValueError:
    print("Invalid input.")

else:
    print("Everything worked fine.")

finally:
    print("Program completed.")


"""
Write a Python program to accept an index from the user and display the corresponding element from a list. 
Handle both ValueError and IndexError exceptions.
"""

try:
    my_list = [10, 20, 30, 40, 50]

    index = int(input("Enter index: "))
    print("Element:", my_list[index])

except ValueError:
    print("Please enter an integer index.")

except IndexError:
    print("Index is out of range.")


"""
Write a Python program to create a dictionary containing student names and marks. Accept a student name from the user 
and display their marks. Handle the KeyError exception if the name does not exist.
"""


try:
    students = {"Rahul": 85, "Aman": 90, "Rohit": 78}

    name = input("Enter student name: ")
    print("Marks:", students[name])

except KeyError:
    print("Student not found.")


"""
Write a Python program to perform an operation on two numbers and use a generic except clause to handle 
any unexpected exception.
"""

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Result:", num1 / num2)

except:
    print("Some error occurred.")
