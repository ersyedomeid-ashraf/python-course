"""
Write a program to ask a number from user. Find the factorial of that number using a loop.
"""

num = int(input("Enter a number = "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print(f"Factorial = {fact}")


"""
Write a program to ask two numbers from user. Print all numbers between those two numbers.
"""


start = int(input("Enter starting number = "))
end = int(input("Enter ending number = "))

for i in range(start, end + 1):
    print(i)
