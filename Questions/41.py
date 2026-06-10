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