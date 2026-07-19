def total_marks(physics, chemistry, biology, maths, english):

    print(f"Your marks in physics = {physics}")
    print(f"Your marks in chemistry = {chemistry}")
    print(f"Your marks in biology = {biology}")
    print(f"Your marks in maths = {maths}")
    print(f"Your marks in english = {english}")

    total = physics + chemistry + biology + maths + english
    print(f"Your total marks = {total}")


total_marks(64, 78, 86, 98, 90)


# Now we used Named Parameter


def total_marks(physics, chemistry, biology, maths, english):

    print(f"Your marks in physics = {physics}")
    print(f"Your marks in chemistry = {chemistry}")
    print(f"Your marks in biology = {biology}")
    print(f"Your marks in maths = {maths}")
    print(f"Your marks in english = {english}")

    total = physics + chemistry + biology + maths + english
    print(f"Your total marks = {total}")


total_marks(chemistry=88, maths=90, english=99, biology=96, physics=80)


# The first two values are given as positional arguments, and the remaining
# values are given as named (keyword) arguments.


def total_marks(physics, chemistry, biology, maths, english):

    print(f"Your marks in physics = {physics}")
    print(f"Your marks in chemistry = {chemistry}")
    print(f"Your marks in biology = {biology}")
    print(f"Your marks in maths = {maths}")
    print(f"Your marks in english = {english}")

    total = physics + chemistry + biology + maths + english
    print(f"Your total marks = {total}")


total_marks(78, 98, maths=90, english=99, biology=96)
