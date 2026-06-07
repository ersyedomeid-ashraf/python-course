"""
Write a program to ask a number from the user. print all the numbers from 1 to that numbers.
"""

num = int(input("Enter a number = "))
for i in range (1, num+1) :
  print(i, end = " ")



"""
Write a program to ask a number from the user. print all the numbers from that number to 1.
"""

num = int(input("Enter a number = "))

for i in range (num, 0, -1) :
    print(i)