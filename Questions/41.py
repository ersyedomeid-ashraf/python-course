"""
Write a program to print the following pattern 

1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1

"""

for i in range (1,6) :
    
    for j in range (i, 0, -1) :
        print(j, end = " ")

    print()


"""
Write a program to print the following pattern 

1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 
6 5 4 3 2 1
7 6 5 4 3 2 1 
8 7 6 5 4 3 2 1 
9 8 7 6 5 4 3 2 1

"""

for i in range (1,10) :

    for j in range (i, 0, -1) :
        print(j, end = " ")

    print()


"""
Write a program to print th following pattern 

5 
5 4 
5 4 3
5 4 3 2
5 4 3 2 1  
"""

for i in range (5, 0, -1) :

    for j in range (5, i-1, -1) :
        print(j, end = " ")

    print()


"""
Write a program to print the following pattern 

5 
4 4 
3 3 3 
2 2 2 2 
1 1 1 1 1 
"""


for i in range (5, 0, -1) :
    
    for j in range (1,6 -i +1) :
        print(i, end = " ")

    print()