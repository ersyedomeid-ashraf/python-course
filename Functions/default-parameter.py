# Default Parameters


def total_marks(physics=0, chemistry=0, biology=0, maths=0, english=0):

    print(f"Your marks in physics = {physics}")
    print(f"Your marks in chemistry = {chemistry}")
    print(f"Your marks in biology = {biology}")
    print(f"Your marks in maths = {maths}")
    print(f"Your marks in english = {english}")

    total = physics + chemistry + biology + maths + english
    print(f"Your total marks = {total}")


total_marks(english=99, maths=96)
