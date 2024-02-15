from datetime import datetime


def main():
    fmt = "Today is {}/{}/{}"
    now = datetime.today()
    print(fmt.format(now.day, now.month, now.year))


if __name__ == "__main__":
    main()
