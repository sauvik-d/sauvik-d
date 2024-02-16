def print_with_border(some_text):
    border = len(some_text) * "#"
    print(border)
    print(some_text)
    print(border)


print_with_border("Hello")
print_with_border("Goodbye")


def wrap_with_border(some_text):
    """ Returns a string of some_text with a line of # signs
            before and after it"""
    result = [len(some_text) * "#"]
    result.append(some_text)
    result.append(result[0])
    return "\n".join(result)


print(wrap_with_border("Hello"))
print("The doc string in:\n", wrap_with_border.__doc__)
def volume(length, width, height):
    return length * width * height


result = volume(4, 8, 7)
print(result)


def volume(length=10, width=5, height=2):
    """Returns the volume of a box for given dimensions"""
    return length * width * height


print(volume(2, 3))
print(volume(2))


def multiply_by(qty, a_list):
    for index, value in enumerate(a_list):
        a_list[index] = value * qty


def process_list(a_list):
    print("Before:", a_list)
    multiply_by(5, a_list)
    print("After:", a_list)


data = [10, 20, 30, 40]
process_list(data)
data = ["Me", "the", "hello"]
process_list(data)


def update_stickers(the_students, sticker):
    for stickers in the_students.values():
        stickers.append(sticker)


def print_students(students):
    for name, stickers in students.items():
        print("{:>8}:".format(name), " ".join(stickers))


students = {'declan': ["🦋", "🦉", "🦂", "🦒"],
            'jill': ["🦆", "🦓", "🦎", "🦁"],
            'sam': ["🦖", "🦂", "🦗"]}

print_students(students)
update_stickers(students, "🦈")
print("*" * 50)
print_students(students)


def the_sum(*args):
    total = 0
    for elem in args:
        total += elem
    return total


total = the_sum(1, 2, 3, 4, 5)
print(total)


def modify(qty, *values, end="\n"):
    for val in values:
        print(qty * val, end=end)


modify(3, "Hello", "Bye", "Sample", end="|")
print()


def print_score(player, **scores):
    total_score = 0
    print("Player:", player)
    for category, score in scores.items():
        print("{0:>15}: {1}".format(category, score))
        total_score += score
    print("{0:>15}: {1}".format("Total", total_score))


print_score("Aiden", Aces=4, Twos=8, FullHouse=25, LgStraight=40)
print_score("Cindy", Twos=4, LgStraight=40, Chance=24, ThreeOfAKind=21)


def demo():
    global count
    count = 0
    print("Inside Function:", count)


count = 5
print("Before Function:", count)
demo()
print("After Function: ", count)


def square(p):
    return p * p


def increment(p):
    return p + 1


def compute(func, lis):
    for index, item in enumerate(lis):
        lis[index] = func(item)


data = [10, 20, 30, 40]
compute(square, data)
print(data)
compute(increment, data)
print(data)
data = ["2", "4", "6", "8"]
# A map object is an iterator that applies function_name to every item of an_iterable, yielding the results.
values = map(int, data)
print(type(values), ":", values)
total = 0
for value in values:
    total += value
print("Sum of numbers in {} = {}".format(data, total))
tests = {"Sally": (89, 78, 99, 88, 92, 98, 95, 78, 88),
         "Doug": (68, 87, 72, 60, 80, 65),
         "Kesha": (98, 87, 99, 78, 99, 80, 98, 50),
         "John": (89, 78, 99, 88, 92, 99, 95, 88, 95, 99)}


def averages(*grades):
    qty = len(grades)
    return sum(grades)/qty


a, b, c, d = tests.values()
x = map(averages, a, b, c, d)
print("Averages: ", list(x))
x = map(averages, *tests.values())
print("Averages: ", list(x))

# A filter object is an iterator that applies function_name to every item of an_iterable, yielding all the results for which the function returns True.


def multiple_of_three(x):
    return x % 3 == 0


results = filter(multiple_of_three, range(2, 51))
for value in results:
    print(value, end=' ')
print()


def add():
    val = input("Enter value to add: ")
    data.append(val)


def delete():
    item = data.pop(0)
    print("removing", item)


def display():
    print("displaying:", data)


def terminate():
    print("terminating")
    exit()


def illegal():
    print("Illegal Selection\n")


data = []
menu = {"1": add, "2": delete, "3": display, "4": terminate}
keys = sorted(menu.keys())
while True:
    print("Make selection:")
    for key in keys:
        print("\t", key, menu[key].__name__)
    key = input(">")

    menu.get(key, illegal)()
