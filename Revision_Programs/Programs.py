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
