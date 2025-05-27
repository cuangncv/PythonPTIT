from decimal import Decimal, ROUND_HALF_UP


class SinhVien:
    def __init__(self, i, ten, d1, d2, d3):
        self.ma = f"SV{i+1:02d}"
        self.ten = self.chuanHoaten(ten)
        self.dtb = Decimal((d1 * 3 + d2 * 3 + d3 * 2) / 8).quantize(Decimal("0.01"), rounding= ROUND_HALF_UP)
    def chuanHoaten (self, ten):
        words = map(str, ten.strip().split())
        hoten = ""
        for x in words:
            hoten += x[0].upper()+x[1:].lower()+" "
        return hoten
    def __str__(self):
        return f"{self.ma} {self.ten}{self.dtb}"
    def __lt__(self, other):
        if self.dtb == other.dtb:
            return self.ma < other.ma
        return self.dtb > other.dtb

a = []
for i in range (int(input())):
    a.append(SinhVien(i, input().strip(), int(input()), int(input()), int(input())))
a.sort()
stt = 1
print(a[0],"1")
for i in range(1, len(a)):
    print(a[i], end=" ")
    if a[i].dtb != a[i-1].dtb:
        stt = i + 1
        print(stt)
    else:
        print(stt)
