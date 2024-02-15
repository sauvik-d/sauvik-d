data = "\t \nabc def\t \n"
result = data.strip()
# strip method removes leading and trailing whitespace
print(result)
print(len(data), ":", len(result))
result = data.rstrip()
print(len(data), ":", len(result))
result = data.lstrip()
print(len(data), ":", len(result))
