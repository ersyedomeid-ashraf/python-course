"""
Exception Handling:- Exception handling is a mechanism used in programming to handle errors
that occur during the execution of a program.
"""

try:
    list = [23, 43, 3, 3, 56, 78, 88]

    print(list[1])
    print(list[3])
    print(list[65])
except:
    print("Some error occurred")


print("Done")
print("Goodbye")


# Aonther one

try:
    numbers = [10, 20, 30, 40, 50]

    print(numbers[0])
    print(numbers[4])
    print(numbers[8])

except:
    print("Some error occurred")

print("Done")


# Another one


try:
    fruits = ["Apple", "Banana", "Mango"]

    print(fruits[1])
    print(fruits[2])
    print(fruits[5])

except:
    print("Index is not available")

print("Goodbye")
