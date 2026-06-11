"""
Write a program to print the following pattern 
       
         * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * * 

"""

for i in range (1,6) :
    for j in range (i,5) :
        print(" ", end = " ")

    for k in range (1,(i*2)) :
        print("*", end = " ") 

    print()  


"""
Print the following pattern 

                * 
              * * *
            * * * * *
          * * * * * * * 
        * * * * * * * * *
      * * * * * * * * * * *
    * * * * * * * * * * * * * 
  * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * *

"""

for i in range (1,9) :
    for j in range (i,9) :
        print(" ", end = " ")

    for k in range ((i*2) -1) :
        print("*", end = " ")

    print()