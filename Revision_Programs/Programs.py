"""
Write a program to ask a number from user. Print all the number from 1 to that number.
"""

num = int(input("Enter a number = "))

i = 1
while i <= num:
    print(i)

    i = i + 1


# if we take in single line


num = int(input("Enter a number = "))

i = 1
while i <= num:
    print(i, end=" ")

    i = i + 1


"""
Write a porgram to convert two lists into a dictionary. Make two list on your own of
same length, and convert them to dictionary.
"""

list1 = ["python", "programming", "good", "bye"]
list2 = [54, "wow", "lalla", 72]

result = {}

for i in range(0, len(list1)):
    result[list1[i]] = list2[i]

print(result)


"""
Write a program to split a given list into two halves.
"""

my_list = [1, 2, 3, 4, 5, 6]


mid = len(my_list) // 2

first_half = my_list[:mid]
second_half = my_list[mid:]

print("First half:", first_half)
print("Second half:", second_half)


"""
Write a program to ask the user for a number. Then, from a list of numbers, remove all the numbers
that can divisible by the number the user entered.
"""

numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]

n = int(input("Enter a number: "))

new_list = []

for num in numbers:
    if num % n != 0:
        new_list.append(num)

print("Original list:", numbers)
print("Updated list:", new_list)


"""
Write a program to print the following pattern 
       
         * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * * 

"""

for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")

    for k in range(1, (i * 2)):
        print("*", end=" ")

    print()


"""
Write a program to calculate the sum of all the number from 1 to 10. 
"""


total = 0

for i in range(1, 11):
    total = total + i


print(f"Your answer is {total}")


my_string = input("Enter a string = ")

if my_string == my_string[::-1]:
    print("It is a palindrome")

else:
    print("It is not a palindrome")


# WAP to create a tuple of 10 integers and display the largest and smallest element.


t = (12, 45, 67, 23, 89, 5, 34, 76, 18, 50)

print("Tuple:", t)
print("Largest Element:", max(t))
print("Smallest Element:", min(t))


# Continue statement

for i in range(1, 11):
    if i == 6:
        continue
    print(i)
    print("done")

print("Program Finish")


# Accessing element

a = [21, 34, 56.6, 78.9, "Ashraf", "BMW", 23.54, 234.78, 45.543]

b = [34, 432, 46.32, 56.787, "Syed", "M5 Competition", 765.8, 98.09]

print(a[3])

print(b[5])


i = ["You", 34, 66, "Win"]

j = [87, 65, "lose", 54]

print((i[-2]), (j[3]))

print(type(a[4]))
print(type(b[3]))
print(type(i[1]))
print(type(j[2]))


"""
Ask two number from user, print which is greatest.
"""

num1 = int(input("Enter number 1 = "))
num2 = int(input("Enter number 2 = "))

if num1 > num2:
    print("Num1 is greatest")

elif num2 > num1:
    print("Num2 is greatest")

else:
    print("Both are equal")


"""
Write a program to check whether a given number is positive, negative or equal to zero. 
"""
# This is method 1 :
num = int(input("Enter a number = "))

if num >= 0:
    if num > 0:
        print("Postive")

    else:
        print("Equal to zero ")

else:
    print("Negative")


# This is method 2 :

if num > 0:
    print("Positive")

else:  # <=0
    if num == 0:
        print("Equal to zero")

    else:
        print("Negative")


# Comparision Operator

a = 87
b = 78
print(a < b)

a = 346
b = 789
print(a > b)

a = 8900
b = 6550
print(a >= b)

a = 4556
b = 8875
print(a <= b)
print(a != b)

a = 9654
b = 2345
print(a != b)

a = 76567
b = 54345
print(a == b)


# Arithmetic Operators


a = 987
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)


print(a**b)
print(a % b)
print(a / b)
print(a // b)


# Logical Operator
"""
Not reverse the result
"""

physics = 86
chemistry = 15

print(physics > 33 and chemistry > 33)
print(physics > 33 or chemistry > 33)

print(physics > 33)
print(not physics > 33)


# int = integer values
x = 65
print(x)
print(type(x))

# int = integer values
x = 72
print(x, type(x))
y = 23.4

# float = decimal values
print(y, type(y))

# str = string/text values
name = "Syed"
print(name, type(name))

# bool = True or False values
adult = True
print(adult, type(adult))

# list = multiple values inside square brackets []
marks = [33, 44, 78, 80, 77]
print(marks, type(marks))

# tuple = multiple values inside parenthesis ()
marks = (80, 77, 50, 65, 36)
print(marks, type(marks))

# dictionary = key-value pairs inside curly braces {}
marks = {"Syed": 70, "Ayush": 35, "Ambani": 19}
print(marks, type(marks))


start = int(input("Enter start number = "))
end = int(input("Enter end number ="))

my_list = [i for i in range(start, end + 1) if i % 2 == 0 and i % 3 == 0]
print(my_list)

"""
Write a program to print the list in descending order 
"""

a = [10, 43, 23, 45, 33, 22, 34, 87, 65, 90, 98, 45]

a.sort()
a.reverse()
print(a)


# list slicing

a = [23, 45, 67, 765, 54, 56, 900, 998, 98, 765, 43]

b = a[3:6]
print(b)


a = [98, 765, 56, 778, 899, 876, 54, 34, 567, 89, 900, 345]

b = a[::-1]
print(b)

# Set programs

my_set = {2, 1, 34, 5, 64, 2, 1, "laila", 88.4, 3, 88.4, 2}

print(my_set)


for i in my_set:
    print(i)

# Another one

my_set = set()

print(my_set)
print(type(my_set))
my_set.add(120)
my_set.add(340)


# methods example

my_set = {4, 5, 6, 7, 8}

print(my_set)

my_set.add(230)

print(my_set)


# membership operator

my_set = {1, 2, 2, 3, 4, 56, 7, 8}

num = int(input("Enter a number = "))

# In the easiest way
if num in my_set:
    print("Yes")

else:
    print("No")
