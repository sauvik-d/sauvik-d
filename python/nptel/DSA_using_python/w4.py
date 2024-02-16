score = {}
score["Test1"] = {}
score["Test2"] = {}
score["Test1"]["Hehe"] = 4
score["Test2"]["Erika"] = 10
score["Test1"]["Dori Indhan Anuprerna"] = 5
print(score)
print(score.keys())
print(list(score.keys()))
print("Sorted DictionaryTest:", sorted(score))
print(score)
d = {}
for l in "abcdefghijkl":
    d[l] = l

print(d["a"])
print(d.keys())
print(d.values())
'''
for n in ["Hehe", "Erika", "Dori Indhan Anuprerna"]:
    total[n] = 0
    for match in score.keys():
        if n in score[match].keys():
            total[n] = total[n] + score[match][n]
print(total)
'''
def func(x, n):
    return x / n
print(func(5, 10))
print(int("75", 8))
x = int(input())
z = 1
if x == 1:
    def f(a, b):
        print(a + b)
else:
    def f(a, b):
        print(a - b)
f(4, 7)
g = f
g(4, 8)
y = 9
if y == 9:
    print("Yes")

def square(x):
    return x * x
def isEven(x):
    return x % 2 == 0
print(list(map(square, filter(isEven, range(100)))))
print([ (x, y, z) for x in range(100) for y in range(100) for z in range(100) if x*x + y*y == z*z ])
