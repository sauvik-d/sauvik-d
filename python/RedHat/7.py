# nested function
def outer(a, b):
    x = 15
    y = 20

    def inner(z):
        print(a, b, x, y, z)
    return inner


result = outer(5, 19)
print(type(result))
result(9)

# functions that are not bound to a name is lambda
# lambda expression must be one-liners, parameters are defined before the colon
# the work of function is defined after the colon, a return statement is unnecessary
print("Lambda application")
results = filter(lambda x: x % 3 == 0, range(2, 51))
for value in results:
    print(value, end=" ")
print()


def outer(a, b):
    x = 15
    y = 20

    return lambda z: print(a, b, x, y, z)


result = outer(5, 10)
print(type(result))
result(9)
# recursion function is a call to itself, a termination condition, when the function does not call itself


def sum_to(n):
    if not n:
        return n
    return n + sum_to(n - 1)


limit = 6
print("Sum from 1 to", limit, "is:", sum_to(limit))
indent = 0
text = "sum_to"


def sum_to(n):
    global indent
    print(" " * indent, text, n)
    indent += 1
    if not n:
        indent -= 1
        print(" " * indent, text, n, "=>", n)
        return n
    result = sum_to(n-1)
    indent -= 1
    print(" " * indent, text, n, end="")
    print(" => {0:2} + {1:2} => {2:2}".format(n, result, n + result))
    return n + result


limit = 6
print("\nSum from 1 to", limit, "is:", sum_to(limit))


def iterative_sum_to(n):
    total = 0
    for i in range(n, 0, -1):
        total += i
    return total


limit = 6
print("Sum from 1 to", limit, "is:", iterative_sum_to(limit))
