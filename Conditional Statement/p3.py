"""
Ask physics and chemistry marks from user 
Print PASS, if student is passed in both subjects 
Else print FAIL
"""

Physics = int(input("Enter Physics marks = "))
Chemistry = int(input("Enter Chemistry marks = "))

if Physics >= 33 and Chemistry >= 33 :
    print("PASS")

else :
    print("FAIL")
