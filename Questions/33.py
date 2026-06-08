"""
Write a program to calculate how many numbers are divisible by both 6 and 7 betwen 1 to 400.
"""

count = 0 

for i in range(1, 400) :
   
    if i%6 == 0 and i%7 == 0 :
        count = count + 1 


print(count)


# Calculate how many numbers are divisible by both 15 and 16 between 1 to 2000.


count = 0 

for i in range(1, 2001) :

    if i%15 == 0 and i%16 == 0 :
        count = count + 1 


print(count)