class Employee:
    pass


class Manager(Employee):
    pass


class Executive(Manager):
    pass


def main():
    manager = Manager()
    print(isinstance(manager, Employee))
    print(isinstance(manager, Manager))
    print(isinstance(manager, Executive))

    print(issubclass(Executive, Executive))
    print(issubclass(Executive, Manager))
    print(issubclass(Executive, Employee))
    print(issubclass(Executive, object))


if __name__ == "__main__":
    main()
