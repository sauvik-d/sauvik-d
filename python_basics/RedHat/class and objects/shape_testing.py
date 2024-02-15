from shape_circle import Circle
from shape_square import Square
from shape_rectangle import Rectangle


def main():
    shapes = [Circle("Circle 1", 10),
              Square("Square 1", 5),
              Rectangle("Rectangle 1", 5, 10)]

    for shape in shapes:
        print(shape)
        print("AREA:", shape.area())
        print("*" * 50)


if __name__ == "__main__":
    main()
