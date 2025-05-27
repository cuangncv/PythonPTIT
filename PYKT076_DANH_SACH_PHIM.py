from datetime import datetime

class Phim:
    def __init__(self, y, matl, ngaykc, ten, soTap):
        self.ma = "P{:03d}".format(y+1)
        self.theLoai = theLoai[int(matl[2:]) - 1]
        self.ngaykc = datetime.strptime(ngaykc, "%d/%m/%Y")
        self.ten = ten
        self.soTap = soTap
    def __str__(self):
        return f"{self.ma} {self.theLoai} {self.ngaykc.strftime('%d/%m/%Y')} {self.ten} {self.soTap}"
    def __lt__(self, other):
        if self.ngaykc == other.ngaykc:
            if self.ten == other.ten:
                return self.soTap > other.soTap
            return self.ten < other.ten
        return self.ngaykc < other.ngaykc

n, m = map(int, input().split())
theLoai = []
for i in range (n):
    theLoai.append(input())
phims = []
for y in range (m):
    p = Phim(y, input(), input(), input(), int(input()))
    phims.append(p)
phims.sort()
for x in phims:
    print(x)