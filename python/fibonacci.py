def fibonacci(x):
    if x <= 1:
        return x
    return fibonacci(x-1) + fibonacci(x-2)


n = int(input("Enter the value of n: "))
print(fibonacci(n))
go = "go"
