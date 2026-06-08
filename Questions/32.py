"""
Wrrite a program to calculate how many numbers are divisible by 7 frim 1 to 100.
"""

count = 0 

for i in range(1, 101) :
    
    if i%7 == 0 :
        count = count + 1 


print(count)



# Calculate how many numbers are divisible by 17 from 1 to 500.


count = 0 

for i in range(1, 501):
    
    if i%17 == 0 :
        count = count +1 


print(count)