import math


class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu // math.gcd(tu, mau)
        self.mau = mau // math.gcd(tu, mau)
    def __add__(self, other):
        ss_tu = self.tu * other.mau + self.mau * other.tu
        ss_mau = self.mau * other.mau
        return PhanSo(ss_tu, ss_mau)
    def __str__(self):
        return '{}/{}'.format(self.tu, self.mau)

if __name__ == '__main__':
    a = input().split()
    p = PhanSo(int(a[0]), int(a[1]))
    q = PhanSo(int(a[2]), int(a[3]))
    print(p+q)