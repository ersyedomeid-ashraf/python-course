"""
Write a program to print the Star Diamond pattern 

       * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

"""

for i in range (1,6) :
   
    for j in range (i,5) :
        print(" ", end = " ")


    for k in range (1, (i*2) ) :
    
        print("*", end = " ")

    print()


for i in range (4,0,-1) :
   
    for j in range (5,i,-1) :
        print(" ", end = " ")


    for k in range (1, (i*2)) :
        
        print("*", end = " ")

    print()



"""
Print the star diamond pattern 

          *
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
* * * * * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          *

          
"""

for i in range (1,12) :
    
    for j in range (i,12) :
        print(" ", end = " ")

    for k in range ((i*2)-1) :
        print("*", end = " ")

    print()


for i in range (11,0,-1) :
    
    for j in range (12,i,-1) :
        print(" ", end = " ")

    for k in range ((i*2)-1) :
        print("*", end = " ")

    print()