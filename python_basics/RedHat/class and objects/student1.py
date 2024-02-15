class Student:

    def __init__(self, name, major):
        self.name = name
        self.major = major


def main():
    jeff = Student("Jeff", "Statistics")
    heather = Student("Heather", "Mathematics")
    print(jeff.name, ":", jeff.major)
    jeff.name = "Jeffrey"
    heather.major = "Computer Science"
    print(jeff.name, ":", jeff.major)
    print(heather.name, ":", heather.major)


if __name__ == "__main__":
    main()

