"""
Write a program take three numbers as input from user and print which one is greater 
or are they equal 

- Print "Fizz" if the number is divisible by 3.
- Pinrt "buzz" if the number is divisible by 5.
- Print "FizzBuzz" if the number is divisible by 3 and 5.
- Print the number itself if none of the conditions are true. 
"""

num = int(input("Enter a number = "))

if num%3 == 0 and num%5 == 0 :
    print("FizzBuzz")

elif num%3 == 0 :
    print("Fizz")

elif num%5 == 0 :
    print("Buzz")

else :
    print(num)
    