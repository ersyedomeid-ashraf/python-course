"""
Write a program to ask a number from user. Find the factorial of that number using a loop.
"""

num = int(input("Enter a number = "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print(f"Factorial = {fact}")
