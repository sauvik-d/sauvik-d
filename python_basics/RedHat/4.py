for i in range(5):
    print(i, end=" ")
print()
for i in range(5, 10):
    print(i, end=" ")
print()
for i in range(-5, 9, 3):
    print(i, end=" ")
print()

text = "This, is, comma, separated, text"
data = text.split(",")
for value in data:
    print(value, end=" ")
print()
text = "Each    word    is  separated   by  whitespace"
data = text.split()
for value in data:
    print(value)
listA = list()
listB = list()
listC = [20, 3, 7, 82, -3, 356, 3, 65, 23]
listD = ["James", "Heather", "Monica", "Eugene"]
listE = listC + listD
print(listA, listB, listC, listD, listE, sep="\n")
print(listC[-1])
subList = listC[0:5]
print(type(subList), subList)
print(listE[-5:])
prompts = ["Please enter some first names ", "again ", "to delete"]
end = "\n" * 2
msg1 = prompts[0]
msg2 = "".join(prompts[:2])
msg3 = "".join(prompts)
name_list = input(msg1).split()
unique_names = set(name_list)
backedup_names = set(unique_names)
print(unique_names, end=end)
name_list = input(msg2).split()
for name in name_list:
    if name not in unique_names:
        unique_names.add(name)
    else:
        print("\t", name, "already existed and is ignored")
print(unique_names, end=end)
print()
print("Original: ", backedup_names)
print("Current: ", unique_names, "\n")
print("Original is subset of Current: ", backedup_names.issubset(unique_names))
print("Current is superset of Original: ", unique_names.issuperset(backedup_names))
name_list = input(msg3).split()
for name in name_list:
    unique_names.discard(name)
print(unique_names, end=end)
print()
print("Original:", backedup_names)
print("Current :", unique_names, "\n")
print("Original is subset of Current ? ", backedup_names.issubset(unique_names))
print("Current is superset of Original ? ", unique_names.issuperset(backedup_names))
# Pop each element from the set until it is empty
print("Popping each name from set: ", unique_names)
while unique_names:
    print(unique_names.pop(), end=" ")
print()
