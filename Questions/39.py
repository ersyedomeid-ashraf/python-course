"""
Write a program to print the following pattern 

1
1 2
1 2 3 
1 2 3 4 
1 2 3 4 5

"""


for i in range (1,6) :
    
    for j in range (1, i + 1) :
        print(j, end = " ")

    print()


"""
1
1 2 
1 2 3 
1 2 3 4
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9 10 
""" 


for i in range (1,11) :
    
    for j in range (1, i +1) :
        print(j, end = " ")

    print()