"""
Write a program to calculate how many numbers are divisible by 7 from 1 to 100.
"""

i = 1
count = 0

while i<=100 :

    if i%7 == 0 :
        count = count + 1
    i = i + 1 


print(count)



# Now if we check how many numbers are divisible by 2 

i = 1 
count = 0 

while i <= 100 :
    
    if i%2 == 0 :
        count = count + 1 
    i = i + 1 


print(count)    



# Now if we check how many numbers are divisible by 5

i = 1 
count = 0 
 
while i <= 100 :
    
    if i%5 == 0 :
        count = count + 1 
    i = i + 1 


print(count)



# Now if check how many numbers are divisible by 19 


i = 1 
count = 0

while i <= 1000 :
    
    if i%19 == 0 :
        count = count + 1
    i = i + 1 


print(count)