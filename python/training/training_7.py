print(2**3)


def raise_to_power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result


print(raise_to_power(4, 3))
# 2D list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[2][1])
for row in number_grid:
    for column in row:
        print(column)


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "S"
            else:
                translation = translation + "s"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))
'''
# Its a comment
'''
# catching error
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
