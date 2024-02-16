class Student:
    """
    This class represents a Student. This multiline string will act as a doc string
    since it is declared at the top of the class.
    """


def main():
    """
    This main is basically for testing purposes only.
    The Student class would typically be imported by
    another module as opposed to running it here.
    """
    jeff = Student()
    heather = Student()
    print(jeff, id(jeff), hex(id(jeff)))
    print(heather, id(heather), hex(id(heather)))


if __name__ == "__main__":
    main()
