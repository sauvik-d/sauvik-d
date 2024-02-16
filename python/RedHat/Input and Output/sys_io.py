import sys


def main():
    sys.stdout.write("Please enter some text:\n")
    x = sys.stdin.readline()
    sys.stdout.write(f"Standard Output\n{x}")
    sys.stderr.write(f"Error Output\n{x}")


if __name__ == "__main__":
    main()
