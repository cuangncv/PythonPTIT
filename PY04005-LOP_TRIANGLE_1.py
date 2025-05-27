import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Triangle:
    def __init__(self, a , b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        AB = self.a.distance(self.b)
        BC = self.b.distance(self.c)
        AC = self.a.distance(self.c)
        return "INVALID" if max(AB, BC, AC) * 2 >= AB + BC + AC else "{:.3f}".format(AB + BC + AC)

a = []
t = int(input())
for i in range (t):
   a += [float(i) for i in input().split()]
i = 0
for _ in range (t):
    A = Point(a[i], a[i+1])
    B = Point(a[i + 2], a[i + 3])
    C = Point(a[i + 4], a[i + 5])
    print(Triangle(A, B, C))
    i += 6