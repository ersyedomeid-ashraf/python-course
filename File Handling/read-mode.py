f = open("File Handling/hello.txt", "r")
x = f.read()
print(x)
f.close()


# Another one

f = open("File Handling/hello.txt", "r")

print(f.read(6))
print(f.read(8))

f.close

# Another one

f = open("File Handling/hello.txt", "r")

print(f.readline())

f.close


# Another one

f = open("File Handling/hello.txt", "r")

print(f.readlines())

f.close


# Another one


f = open("File Handling/hello.txt", "r")
x = f.read()
print(x)

print(f.read(6))
print(f.read(8))

print(f.readline())

print(f.readlines())

f.close()
