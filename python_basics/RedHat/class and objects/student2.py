class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_major(self):
        return self.major

    def set_major(self, major):
        self.major = major



def main():
    jeff = Student("Jeff", "Statistics")
    print(jeff.get_name(), ":", jeff.get_major())
    jeff.set_name("Jeffrey")
    print(jeff.get_name(), ":", jeff.get_major())


if __name__ == "__main__":
    main()
