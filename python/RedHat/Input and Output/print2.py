def main():
    with open('output4', 'w') as a_file:
        while True:
            data = input("Enter data ('q' to exit): ")
            if data == "q":
                break
            print(data, file=a_file)

        print("File is now closed? ", a_file.closed)


if __name__ == "__main__":
    main()
