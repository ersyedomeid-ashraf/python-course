"""
A student will not be allowed to sit in exam if his/her attendance is less than 75%.
"""

# Take following inout from the user :-
# Number of classes held 
# Number of classes attended. 
# 1 Print percentage of classes attended 
# 2 print is student is allowed to sit in exam or not.


class_held = int(input("Enter total classes held = "))
class_attended = int(input("Enter total classes attended = "))

class_per = (class_attended/class_held)*100
print(f"Percentage of class attended = {class_per}%") 


#print(f"Percentage of class attended = {class_per:.2f}%")
#{class_per:.2f} is used to limit a float valuse to two decimal places.
# For ex, if the result is 23.444444, using {:.2f} will display it as 23.44
#  This makes th output cleaner and easier to read.   
                                                                      

if class_per >= 75 :
    print("Yes, you can sit in your exam")

else :
    print("No, you cannot sit in your exam")
 