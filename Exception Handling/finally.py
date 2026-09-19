try:
    my_list = [7, 3, 9, 4, 2]

    print(my_list[3])

except IndexError:

    print("Invalid Index")

except ZeroDivisionError:

    print("You cannot divide by zero")

except:

    print("Some error occurred")

else:  # It's not a compulsory

    print("Everything worked fine")

finally:

    print("This is a finally clause")
