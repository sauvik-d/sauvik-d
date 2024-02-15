def func():
    print("It's a function")


print("Okay")
func()
print("Got it")


def func_with_arg(name, roll):
    print("Hello " + name + ". your roll is", int(roll))


func_with_arg("Sauvik", 720)


def cube(num):
    return num*num*num


result = cube(4)
print(result)

is_male = True
is_tall = True
if is_male or is_tall:
    print("You are a male")
elif not is_tall and is_male:
    print("You are a short male")


is_cloudy = False
if is_cloudy:
    print("Its Cloudy")
else:
    print("Its not Cloudy")


# max between three numbers
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(4, 6, 8))
# basic calculator
var1 = float(input("Enter first number: "))
var2 = float(input("Enter second number: "))
op = input("Enter operator: ")

if op == "+":
    print(var1 + var2)
elif op == "-":
    print(var1 - var2)
elif op == "*":
    print(var1 * var2)
elif op == "/":
    print(var1 / var2)
else:
    print("Invalid operator")



