"""
Write a Python program to create a file and write some text into it.
"""

f = open("demo.txt", "w")

f.write("Hello Python\n")
f.write("File Handling")

f.close()

print("Data written successfully")
