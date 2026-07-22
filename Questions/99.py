"""
Write a program to write a function that takes an integer and prints whether
it is a prime number.
"""


def is_prime(num):  # 30

    factors = 0

    for i in range(1, num + 1):  # 1 2 3 4 5 6......28 29 30

        if num % i == 0:
            factors += 1

    if factors == 2:
        print("It is a prime number")

    else:
        print("It is not a prime number")


is_prime(10)
is_prime(11)


# Another one


def is_prime(num):  # 99

    factors = 0

    for i in range(1, num + 1):  # 30 31 32.......98 99

        if num % i == 0:
            factors += 1

    if factors == 2:
        print("It is a prime number")

    else:
        print("It is not a prime number")


is_prime(76)
is_prime(13)
is_prime(86)
is_prime(12)
is_prime(78)
is_prime(24)
is_prime(18)
