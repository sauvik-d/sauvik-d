def main():
    print("testing my functions at top level", square(5), cube(10))

def square(p):
    return p ** 2

def cube(p):
    return p ** 3

if __name__ == "__main__":
    main()
