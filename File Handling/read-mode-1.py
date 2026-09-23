with open("File Handling/hello.txt", "r") as f:

    x = f.read()

    for ch in x:

        print(ch)


# Another one

with open("File Handling/hello.txt", "r") as f:

    for line in f:

        print(line)

#  OR

with open("File Handling/hello.txt", "r") as f:

    for line in f:

        print(line, end=" ")
