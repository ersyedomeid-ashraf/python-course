"""
Write a program to print the following number pattern
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""

for i in range(1,6) :
    for j in range(1,6) :
        print(i, end = " ")

    print()



"""
Write a program to print the following number pattern 
5 5 5 5 5 
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1 
"""

for i in range(6, 0, -1) :
    for j in range(1,6):
        print(i,end = " ")

    print()




"""
Write a program to ask N from user. N means number of lines. Then print the following pattern 

Enter number = 5

1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5 
"""

n = int(input("Enter a number = "))

for i in range (1, n+1) :
    for j in range (1,6) :
        print(i, end = " ")

    print()





"""
Write a program to ask N user. N means of lines. Then print the following pattern 

Enter a number = 4

4 4 4 4 4
3 3 3 3 3
2 2 2 2 2 
1 1 1 1 1
"""


n = int(input("Enter a number = "))

for i in range (n, 0, -1) :
    for j in range (1,6) :
        print(i, end = " ")

    print()