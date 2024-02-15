class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def translate(self, deltax, deltay):
        self.x += deltax
        self.y += deltay

    def __str__(self):
        return ('('+str(self.x)+','+str(self.y)+')')


p = Point(3, 2)
p.translate(2, 1)
p2 = Point(8, 2)
p2.translate(2, 5)
print(p2.y)
print(p.x)
print(p.y)
hehe = p.__str__()
print(hehe)
print(p)

