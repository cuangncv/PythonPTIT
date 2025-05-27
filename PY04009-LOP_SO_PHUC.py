class SoPhuc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return SoPhuc(self.a + other.a, self.b + other.b)
    def __mul__(self, other):
        thuc = self.a * other.a - self.b * other.b
        ao = self.a * other.b + self.b * other.a
        return SoPhuc(thuc, ao)
    def __str__(self):
        if self.b > 0:
            return f"{self.a} + {self.b}i"
        elif self.b == 0:
            return f"{self.a}"
        else:
            return f"{self.a} - {abs(self.b)}i"

for i in range(int(input())):
    a = list(map(int, input().split()))
    A, B = SoPhuc(a[0], a[1]), SoPhuc(a[2], a[3])
    print(f"{(A+B) * A}, {(A+B) * (A+B)}")