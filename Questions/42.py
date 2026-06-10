"""
Write a program to print the following pattern 

*
* * 
* * * 
* * * * 
* * * * * 

"""

for i in range (1,6) :

    for j in range (i) :
        print("*", end = " ")

    print()


"""

 Print the following pattern 

 * * * * * 
 * * * *
 * * *
 * * 
 *

"""


for i in range (5,0,-1) :

    for j in range (i) :
        print("*", end = " ")

    print()