"""
Write a program to write a funtion that takes a list of number and prints the
sum and average of these numbers.
"""


def sum_avg_lst(lst):

    total = 0

    for num in lst:
        total = total + num

    print(f"Total of all numbers = {total}")

    avg = total / len(lst)
    print(f"Average of all numbers = {avg}")


sum_avg_lst([1, 2, 3, 4, 5])
sum_avg_lst([59, -86, 74, 102, 97])
