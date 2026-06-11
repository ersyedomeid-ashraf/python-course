"""
Write a program to print the following pattern 

5 
4 5 
3 4 5 
2 3 4 5
1 2 3 4 5 
"""


for i in range (5,0,-1) :
    for j in range (i,6) :
        print(j, end = " ")

    print()


"""
Print the following pattern 

5 4 3 2 1 
5 4 3 2
5 4 3
5 4 
5
"""

for i in range (5,0,-1) :
    for j in range (5,i-1,-1) :
        print (j, end = " ")

    print()


"""
print the following pattern 

5 5 5 5 5 
4 4 4 4
3 3 3 
2 2 
1 
"""

for i in range (5,0,-1) :
    for j in range (i) :
        print(i, end = " ")

    print()