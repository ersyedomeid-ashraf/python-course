# Multiple Exception Handling

try:
    my_list = [87, 67, 99, 62, 22]

    print(my_list[3])
    print(my_list[2])
    print(my_list[78])

except IndexError:

    print("Invalid Index")


try:
    my_list = [2, 5, 6, 7, 88, 0]

    print(my_list[0] / my_list[-1])

except ZeroDivisionError:

    print("You cannot divide by zero")


try:
    my_list = [2, 5, 6, 7, 88, 0]
    # print(my_list[78])
    # print(my_list[0] / my_list[-1])
    my_list = my_list * "abc"

except IndexError:

    print("Invalid Index")

except ZeroDivisionError:

    print("You cannot divide by zero")

except:

    print("Some error occurred")
