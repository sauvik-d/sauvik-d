def function():
    integer = input("Please enter a +ve integer ")
    if integer.isnumeric():
        return integer
    else:
        return 0


value = function()

if not value:
    print("It is an invalid input!")
else:
    print(value)
