for i in reversed(range(1, 100)):
    fmt = "{0} bottles of water on the wall!\n{0} bottles of water!\nTake one down\nAnd pass it around\n{1} bottles of water on the wall!"
    if i >= 2:
        print(fmt.format(i, i - 1))
        print()
    else:
        print(fmt.format(i, "No"))
        print()


