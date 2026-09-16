# Multiple Exception Handling

try:
    my_list = [87, 67, 99, 62, 22]

    print(my_list[3])
    print(my_list[2])
    print(my_list[78])

except IndexError:

    print("Invalid Index")
