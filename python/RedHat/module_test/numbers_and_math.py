import math
import decimal
import random


def math_examples():
    print("Square root of 10:", math.sqrt(10))
    print(math.pow(64, 1.5))
    print("Hypotenuse of 6 and 8 ", math.hypot(6, 8))
    print("Smallest integer >= 2.5", math.ceil(2.5))
    print(math.pi)


def decimal_examples():
    print(.1 + .2)
    d1, d2 = decimal.Decimal(".1"), decimal.Decimal(".2")
    print("It is normally: ", d1 + d2)


def random_examples():
    data = [9, 8, 7, 6, 5, 4, 3, 2]
    print(random.random())
    print(random.randrange(10))
    print("Choice ", data, ":", random.choice(data))
    random.shuffle(data)
    print(data)
    print(random.sample(data, 4))
