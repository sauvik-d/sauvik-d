numbers = [10, 20, 30, 40, 50]
fmt = "{0:>24} {1}"
print(fmt.format("Original: ", numbers))
print(fmt.format("Pop Last Element: ", numbers.pop()))
print(fmt.format("Pop Element at pos #2: ", numbers.pop(2)))
print(fmt.format("Resulting List: ", numbers))
numbers.append(100)
print(numbers)
numbers.remove(20)
print(numbers)
print(numbers)
numbers.insert(1, 1000)
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
mon, tue, wed, thu, fri = days
print(mon, fri)
for day in days:
    print(day, end="\t")
print()
for index in range(len(days)):
    days[index] *= 10
grades = ("A", "B", "C", "D", "E")
for i, grade in enumerate(grades, start=1):
    print(i, ":", grade, end="\t")
print()
setB = set("mississippi")
print("Length of setB:", len(setB))
print(setB)
fruit = {"apple", "orange", "pear", "kiwi"}
print("orange" in fruit, ":", "crabgrass" in fruit)

