"""
Write a program to replace a substring in a given string.
"""

s = input("Enter a string : ")

print("No String:", s.replace("old", "new"))


"""
Write a program to calculate the electricity bill based on given conditions.
"""

units = int(input("Enter units = "))
if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7

else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print("Bill:", bill)
