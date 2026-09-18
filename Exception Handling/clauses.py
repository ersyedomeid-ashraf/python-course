try:
    my_list = [87, 67, 99, 62, 22]

    print(my_list[3])

except IndexError:

    print("Invalid Index")

except ZeroDivisionError:

    print("You cannot divide by zero")

except:

    print("Some error occurred")

else:  # It's not a compulsory

    print("Everything worked fine")
