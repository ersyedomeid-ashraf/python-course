file_name = input("Enter a file name (without extension)=")
file_name = file_name + ".txt"

with open(file_name, "w") as f:

    while True:
        sentence = input("Enter a sentence =")

        if sentence == "q" or sentence == "Q":
            break

        f.write(sentence)
        f.write("\n")


# Another one

file_name = input("Enter file name = ")
file_name = file_name + ".txt"

with open(file_name, "w") as f:

    while True:
        item = input("Enter item = ")

        if item == "q" or item == "Q":
            break

        f.write(item)
        f.write("\n")
