"""
Write a program to calculate the sum of all the numbers are divisible by 4 from 20 to 60.
"""

total = 0 

for i in range(20, 61) :

    if i%4 == 0 :
        total = total + i 


print(total)