def main():
    with open(input("enter a file name: "), "r") as the_file:
        for a_line in the_file:
            print(a_line, end="")


if __name__ == "__main__":
    main()
