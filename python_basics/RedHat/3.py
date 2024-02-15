result = input("Enter a number:")
number = int(result)
fmt = "Base 10: {}\tBase 2: {}\tBase 8: {}\tBase 16: {}"
print(fmt.format(int(result), int(result, 2), int(result, 8), int(result, 16)))
# conversions to a float
a_float = input("Enter a decimal number:")
sum_of_input = float(a_float) + float(result)
print(sum_of_input)
fmt = "Binary: {}\tOctal: {}\tHexadecimal: {}"
print(fmt.format(bin(number), oct(number), hex(number)))
print(ord("A"), chr(66))
print(float("982"))
print(int(98.76))


