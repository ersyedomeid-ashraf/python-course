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


# list common example

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8, 9]

c = set(a)
d = set(b)

result = list(c.intersection(d))
print(result)


# Calculate how many numbers are divisible by both 15 and 16 between 1 to 2000.


count = 0

for i in range(1, 2001):

    if i % 15 == 0 and i % 16 == 0:
        count = count + 1


print(count)

"""
Write a porgram that reverse each word in a sentence while maintaining the word order.
For example, "Hello" should become "olleH"
"""

my_string = "python is good"
words = my_string.split()

result = " ".join(i[::-1] for i in words)
print(result)


# Write a program to do arithmetical operations addition and division

# Addition
num1 = float(input("Enter the first number for addition = "))
num2 = float(input("Enter the second number for addition = "))

sum_result = num1 + num2

print(f"sum: {num1} + {num2} = {sum_result}")

# Division
num3 = float(input("Enter the dividend for division = "))
num4 = float(input("Enter the division for division = "))

if num4 == 0:
    print("Error : Division by zero is not allowed .")

else:
    div_result = num3 / num4
    print(f"Division : {num3}/{num4} = {div_result}")


# Write a program to swap two variables.

a = input("Enter the value of the first variable (a) = ")
b = input("Enter the value of the second variable (b) = ")

print(f"Original values : a = {a}, b = {b}")

temp = a
a = b
b = temp

print(f"Swapped values: a={a}, b = {b}")


# Write a program to generate a random number.

import random

print(f"Random number: {random.randint(1, 100)}")


# Write a program to convert kilometer to miles.

kilometers = float(input("Enter distance in kilometer = "))


# Conversion factor : 1 kilometer = 0.621371 miles

conversion_factor = 0.621371

miles = kilometers * conversion_factor

print(f"{kilometers} kilometers is equal to {miles} miles")


# Write a program to display calendar .

import calendar

year = int(input("Enter a year = "))
month = int(input("Enter a month = "))

cal = calendar.month(year, month)

print(cal)

# Write a program to find the factorial of a number .

num = int(input("Enter a number = "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")

elif num == 0:
    print("Factorial of 0 is 1")

else:
    for i in range(1, num + 1):
        factorial = factorial * i

    print(f"The factorial of {num} is {factorial}")


"""
Print the star diamond pattern 

          *
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
* * * * * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          *

          
"""

for i in range(1, 12):

    for j in range(i, 12):
        print(" ", end=" ")

    for k in range((i * 2) - 1):
        print("*", end=" ")

    print()


for i in range(11, 0, -1):

    for j in range(12, i, -1):
        print(" ", end=" ")

    for k in range((i * 2) - 1):
        print("*", end=" ")

    print()


"""
Write a program to remove all elements from a given sets.
"""

my_set = {34, 54, 46, 78, 98}

my_set.clear()
print(my_set)


my_set = {34, 32, 56, 78, 98, 766, 778, 90}

my_set.clear()
print(my_set)


my_set = {33, 45, 90, 98, 77, 67, 68, 78, 98, 56, 4556, 778887, 544, 5678, 889}

my_set.clear()
print(my_set)


"""
Write a program to find common elements in three lists using sets.
"""

list1 = [45, 3, 4, 4, 5, 56, "laila", 67, 76, 5, 4, 3, 4556, "tinaa", 654, 767, 678]
list2 = [4, 5, 654, 45, 789, 78, 899, 87, 667, 66, 55, "laila"]
list3 = [5, 4, 3, "laila", "tina", 45, 4556, 654, 767]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

x = set1.intersection(set2)
result = x.intersection(set3)

print(result)


"""
Write a program to store name as key, and 5 marks in a List as a value in dictionary. Store details
of at least 5 students. Print the name of the student who got highest marks.
"""

student_data = {
    "Satish": [67, 76, 87, 98, 90],
    "Dilip": [89, 98, 76, 78, 56],
    "Rajesh": [89, 76, 67, 90, 78],
    "Munna": [76, 89, 90, 66, 65],
    "Umesh": [98, 78, 67, 99, 90],
}

highest_marks = 0
highest_student_name = ""

for name, marks in student_data.items():
    total = sum(marks)

    if total > highest_marks:
        highest_marks = total
        highest_student_name = name


print(highest_student_name)
print(highest_marks)


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


"""
Write a program to reverse the order of words.
"""

my_string = "Python is good"

words = my_string.split()
print(words)

words = words[::-1]

result = " ".join(i for i in words)
print(result)


"""
Write a program to ask a string from user. Count how many alphabets are
there in that string.
"""

my_string = "abcd1234"

count = 0

for ch in my_string:
    if ch.isalpha():
        count = count + 1

print(count)


# Count alphabets using ASCII values.

my_string = "abcd1234"

count = 0

for ch in my_string:
    ascii = ord(ch)

    if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
        count += 1

print(count)


"""
Write a program to make your own list. Find the sum of all even numbers present in that list.
"""

my_list = [11, 23, 22, 44, 53, 65, 45, 88, 94, 20, 50]

total = 0

for i in range(0, len(my_list)):

    if my_list[i] % 2 == 0:
        total = total + my_list[i]


print(total)


"""
Write a program to write a function that accepts an integer and prints the
multiplication table for that number up to 10.
"""


def multiplication_table(num):
    for i in range(1, 11):

        print(f"{num} x {i} ={num*i}")


multiplication_table(87)


"""
Write a program to write a function that accepts an integer and prints whether it is odd or even
"""


def even_odd(num):
    if num % 2 == 0:
        print("It is a even number")

    else:
        print("It is a odd number")


even_odd(10)
even_odd(9)


# Another one


def even_odd(num):
    if num % 2 == 0:
        print("It is a even number")

    else:
        print("It is a odd number")


even_odd(64)
even_odd(99)


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


largest(9845674, 859057, 5875894)


"""
Write a program to write a function that takes an integer and prints whether
it is a prime number.
"""


def is_prime(num):  # 30

    factors = 0

    for i in range(1, num + 1):  # 1 2 3 4 5 6......28 29 30

        if num % i == 0:
            factors += 1

    if factors == 2:
        print("It is a prime number")

    else:
        print("It is not a prime number")


is_prime(10)
is_prime(11)


"""
Write a program to write a funtion that takes a list of number and prints the
sum and average of these numbers.
"""


def sum_avg_lst(lst):

    total = 0

    for num in lst:
        total = total + num

    print(f"Total of all numbers = {total}")

    avg = total / len(lst)
    print(f"Average of all numbers = {avg}")


sum_avg_lst([1, 2, 3, 4, 5])
sum_avg_lst([59, -86, 74, 102, 97])


# Another one


def sum_avg_lst(lst):

    total = 0

    for num in lst:
        total = total + num

    print(f"Total of all numbers = {total}")

    avg = total / len(lst)
    print(f"Average of all numbers = {avg}")


sum_avg_lst([8, 7, 6, 5, 44, 56, 78, 90])
sum_avg_lst([98, -54, 898, 900, 787, 546, -8677, 988])


"""
Write a program to write a function that accepts a string and prints the
frequency of each character in the string.

Example - HELLO

{"H":1, "E":1, "L":2, "O":1}

h occurs 1 times
e occurs 1 times
l occurs 2 times
o occurs 1 times
"""


def charCount(string):

    my_dict = dict()

    for ch in string:

        if ch not in my_dict:
            my_dict[ch] = 1

        else:
            my_dict[ch] += 1

    for k, v in my_dict.items():
        print(f"{k} occurs {v} times")


charCount("HEELLLLLOOOOOOOOOOO")


"""
Write a program to write a function that takes a string and prints whether
it is a palindrome.
"""


def check_palindrome(string):

    if string == string[::-1]:
        print("It is a palindrome")

    else:
        print("It is not a palindrome")


check_palindrome("mom")
check_palindrome("anaa")
check_palindrome("madam")


"""
Write a program to ask a string from a user, remove all the duplicates from that string
and print hat string again (order doesn't matter).
"""

my_string = "aaaaaaeeeerrrrooooppppllllaaaannnneeee"

result = set(my_string)
print(result)
joined_string = " ".join(result)
print(joined_string)


"""
Write a program to find the length of a set.
"""

my_set = {45, 87, 77, 90, "Majnu", 34}

count = 0
for i in my_set:
    count += 1

print(count)

# in short way we'll write

print(len(my_set))


"""
Write a program to create 3 set of your own, find the union of three sets.
"""

list1 = [45, 3, 4, 4, 5, 56, "laila", 67, 76, 5, 4, 3, 4556, "tinaa", 654, 767, 678]
list2 = [4, 5, 654, 45, 789, 78, 899, 87, 667, 66, 55, "laila"]
list3 = [5, 4, 3, "laila", "tina", 45, 4556, 654, 767]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

print(set1 | set2 | set3)


"""
Write a program to write a function that takes a string and prints whether
it is a palindrome.
"""


def check_palindrome(string):

    if string == string[::-1]:
        print("It is a palindrome")

    else:
        print("It is not a palindrome")


check_palindrome("mom")
check_palindrome("anaa")
check_palindrome("madam")


# Another one


def check_palindrome(string):

    if string == string[::-1]:
        print("It is a palindrome")

    else:
        print("It is not a palindrome")


check_palindrome("kuchu puchu")
check_palindrome("civic")
check_palindrome("refer")
check_palindrome("anaaa")
check_palindrome("rotator")


"""
Write a program to write a function that accepts a string and prints the
frequency of each character in the string.

Example - HELLO

{"H":1, "E":1, "L":2, "O":1}

h occurs 1 times
e occurs 1 times
l occurs 2 times
o occurs 1 times
"""


def charCount(string):

    my_dict = dict()

    for ch in string:

        if ch not in my_dict:
            my_dict[ch] = 1

        else:
            my_dict[ch] += 1

    for k, v in my_dict.items():
        print(f"{k} occurs {v} times")


charCount("HEELLLLLOOOOOOOOOOO")


# Another one


def charCount(string):

    my_dict = dict()

    for ch in string:

        if ch not in my_dict:
            my_dict[ch] = 1

        else:
            my_dict[ch] += 1

    for k, v in my_dict.items():
        print(f"{k} occurs {v} times")


charCount("DHARMENDRA PRADHAN ISTIFA DOOOO")


# Default Parameters


def total_marks(physics=0, chemistry=0, biology=0, maths=0, english=0):

    print(f"Your marks in physics = {physics}")
    print(f"Your marks in chemistry = {chemistry}")
    print(f"Your marks in biology = {biology}")
    print(f"Your marks in maths = {maths}")
    print(f"Your marks in english = {english}")

    total = physics + chemistry + biology + maths + english
    print(f"Your total marks = {total}")


total_marks(english=99, maths=96)


def total_marks(physics=0, chemistry=0, biology=0, maths=0, english=0):

    print(f"Your marks in physics = {physics}")
    print(f"Your marks in chemistry = {chemistry}")
    print(f"Your marks in biology = {biology}")
    print(f"Your marks in maths = {maths}")
    print(f"Your marks in english = {english}")

    total = physics + chemistry + biology + maths + english
    print(f"Your total marks = {total}")


total_marks(english=99, chemistry=97, maths=96)


def total_marks(physics, chemistry, biology, maths, english):

    print(f"Your marks in physics = {physics}")
    print(f"Your marks in chemistry = {chemistry}")
    print(f"Your marks in biology = {biology}")
    print(f"Your marks in maths = {maths}")
    print(f"Your marks in english = {english}")

    total = physics + chemistry + biology + maths + english
    print(f"Your total marks = {total}")


total_marks(64, 78, 86, 98, 90)


# Now we used Named Parameter


def total_marks(physics, chemistry, biology, maths, english):

    print(f"Your marks in physics = {physics}")
    print(f"Your marks in chemistry = {chemistry}")
    print(f"Your marks in biology = {biology}")
    print(f"Your marks in maths = {maths}")
    print(f"Your marks in english = {english}")

    total = physics + chemistry + biology + maths + english
    print(f"Your total marks = {total}")


total_marks(chemistry=88, maths=90, english=99, biology=96, physics=80)


# The first two values are given as positional arguments, and the remaining
# values are given as named (keyword) arguments.


def total_marks(physics, chemistry, biology, maths, english):

    print(f"Your marks in physics = {physics}")
    print(f"Your marks in chemistry = {chemistry}")
    print(f"Your marks in biology = {biology}")
    print(f"Your marks in maths = {maths}")
    print(f"Your marks in english = {english}")

    total = physics + chemistry + biology + maths + english
    print(f"Your total marks = {total}")


total_marks(78, 98, maths=90, english=99, biology=96)


# Another one


def total_marks(physics, chemistry, biology, maths, english):

    print(f"Your marks in physics = {physics}")
    print(f"Your marks in chemistry = {chemistry}")
    print(f"Your marks in biology = {biology}")
    print(f"Your marks in maths = {maths}")
    print(f"Your marks in english = {english}")

    total = physics + chemistry + biology + maths + english
    print(f"Your total marks = {total}")


total_marks(chemistry=89, maths=98, english=75, biology=66, physics=90)


def add():

    num1 = int(input("Enter a num1 = "))
    num2 = int(input("Enter a num2 = "))

    print(f"Sum {num1 + num2}")


add()


def add():

    num1 = int(input("Enter a num1 = "))
    num2 = int(input("Enter a num2 = "))
    num3 = int(input("Enter a num3 = "))
    num4 = int(input("Enter a num4 = "))
    num5 = int(input("Enter a num5 = "))
    num6 = int(input("Enter a num6 = "))

    print(f"Sum {num1 + num2 + num3 + num4 + num5}")


add()


def sub():

    num1 = int(input("Enter a num1 = "))
    num2 = int(input("Enter a num2 = "))
    num3 = int(input("Enter a num3 = "))
    num4 = int(input("Enter a num4 = "))
    num5 = int(input("Enter a num5 = "))
    num6 = int(input("Enter a num6 = "))
    num7 = int(input("Enter a num7 = "))
    num8 = int(input("Enter a num8 = "))
    num9 = int(input("Enter a num9 = "))
    num10 = int(input("Enter a num10 = "))

    print(f"Sub {num1 - num2}")


sub()


# Write a program to Create a function square(n) that prints the square of a number.


def square(n):
    print(n * n)


num = int(input("Enter a number: "))

square(num)


def check_palindrome(string):

    if string == string[::-1]:
        print("It is a palindrome")

    else:
        print("It is not a palindrome")


check_palindrome("kuchu puchu")
check_palindrome("civic")
check_palindrome("refer")
check_palindrome("anaaa")
check_palindrome("rotator")


"""
Write a program that takes a character as input and prints whether 
it's vowels or constant.
"""

char = input("Enter a character = ")

if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print("Vowel")

else:
    print("Consonant")


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
Write a program to calculate the sum of all the number from 1 to 10. 
"""


total = 0

for i in range(1, 11):
    total = total + i


print(f"Your answer is {total}")


# Calculate the sum of all the number from 1 to 200.


total = 0

for i in range(1, 200):
    total = total + i


print(f"Your answer is {total}")


"""
Write a program to print the following pattern 

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 

"""

for i in range(1, 6):

    for j in range(1, i + 1):
        print(i, end=" ")

    print()


"""
Write a program to make your own list. Print all the elements present at even index position.
"""

my_list = [21, 43, 45, 32, "Hurray", 89, 76, "Done", "Done"]


# Iteration by index

for i in range(0, len(my_list)):
    if i % 2 == 0:
        print(my_list[i], end=" ")


"""
Write a program to ask the user for a number. Then, from a list of numbers, remove all the numbers
that can divisible by the number the user entered.
"""

numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]  # List of numbers

n = int(input("Enter a number: "))  # Ask the user for a number

new_list = []  # Create a new list

for num in numbers:  # Add only numbers that are not divisible by n
    if num % n != 0:
        new_list.append(num)

print("Original list:", numbers)
print("Updated list:", new_list)


"""
Write a program to make  your own list. Find the sum of all numbers divisible by 3 and 4 in that list.
"""

my_list = [12, 24, 33, 36, 45, 60, 64, 54, 84, 600]

total = 0

for i in my_list:

    if i % 3 == 0 and i % 4 == 0:
        total = total + i


print(total)


"""
Write a program to take 10 integer input from user and store them in a list. Now, copy all
the elements in another list but in reverse oreder
"""

my_list = []
for i in range(5):
    value = int(input("Enter value at index {i} = "))
    my_list.append(value)


result = []

for i in range(len(my_list) - 1, -1, -1):
    result.append(my_list[i])
print(result)


"""
Make a program that takes a list of integers and returns the product
of all the elements.
"""

my_list = [23, 54, 65, 45, 98, 77]

product = 1

for num in my_list:
    product = product * num

print(product)


"""
Write a program to ask a string from user. Count the number of uppercase and lowercase
character in that string.
"""

my_string = "abcde12345ABCD"

lower_count = 0
upper_count = 0

for ch in my_string:
    if ch.isupper():
        upper_count += 1

    elif ch.islower():
        lower_count += 1

print(upper_count)
print(lower_count)


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


"""
Store "name" of a student as Key, "list of 5 marks" of that student as a Value.
Store atleast 5 student names. Print the sum and percentage of all the students.
"""

students_data = {
    "student1": [87, 67, 65, 45, 66],
    "student2": [55, 67, 87, 98, 90],
    "student3": [87, 65, 67, 65, 33],
    "student4": [90, 86, 43, 67, 87],
    "student5": [90, 89, 98, 87, 67],
}


for name, marks in students_data.items():
    total = sum(marks)
    percentage = total / 500 * 100
    print(f" {name} has scored total {total} marks, percentage = {percentage:.2f}")


"""
Write a program to find common elements in three lists using sets.
"""

list1 = [
    45,
    3,
    4,
    4,
    5,
    56,
    "laila",
    67,
    76,
    "Kaaalu",
    4,
    3,
    4556,
    "tinaa",
    654,
    767,
    678,
]
list2 = [4, 5, 654, 45, 789, 78, "Kaaalu", 899, 87, 667, 66, 55, "laila"]
list3 = [5, 4, 3, "laila", "tina", 45, 4556, "Kaaalu", 654, 767]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

x = set1.intersection(set2)
result = x.intersection(set3)

print(result)


"""
Write a program to ask a string from a user, remove all the duplicates from that string
and print hat string again (order doesn't matter).
"""

my_string = "MMMMMMMMiiiiiiiiiiiyyyyyyyaaaaaaaaHHHHHHHuuuuuzzzzzzzuuuuurrrrrrrrr"

result = set(my_string)
print(result)
joined_string = " ".join(result)
print(joined_string)


"""
Write a program to write a function that accepts an integer and prints the
multiplication table for that number up to 10.
"""


def multiplication_table(num):
    for i in range(1, 11):

        print(f"{num} x {i} ={num*i}")


multiplication_table(6)


# Another one


def multiplication_table(num):
    for i in range(1, 11):

        print(f"{num} x {i} ={num*i}")
