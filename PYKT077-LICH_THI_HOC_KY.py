from datetime import datetime


class LichThi:
    def __init__(self, i, maMon, ngay, gio, nhom):
        self.maCa = f"T{i+1:03d}"
        self.maMon = maMon
        self.tenMon = ten[self.maMon]
        self.ngay = datetime.strptime(ngay, '%d/%m/%Y')
        self.gio = datetime.strptime(gio, "%H:%M")
        self.nhom = nhom
    def __str__(self):
        return f"{self.maCa} {self.maMon} {self.tenMon} {self.ngay.strftime('%d/%m/%Y')} {self.gio.strftime('%H:%M')} {self.nhom}"
    def __lt__(self, other):
        if self.ngay == other.ngay:
            if self.gio == other.gio:
                return self.maMon < other.maMon
            return self.gio < other.gio
        return self.ngay < other.ngay

n, m = map(int, input().split())
ten = {}
a = []
for i in range (n):
    ma = input().strip()
    ten[ma] = input().strip()
for i in range (m):
    maMon, ngay, gio, nhom = map(str, input().split())
    a.append(LichThi(i, maMon, ngay, gio, nhom))
a.sort()
for x in a:
    print(x)