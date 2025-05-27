class MatHang:
    def __init__(self, ma, ten, sl, gia, chietkhau):
        self.ma = ma
        self.ten = ten
        self.sl = sl
        self.gia = gia
        self.chietkhau = chietkhau
        self.tongtien = self.gia * self.sl - self.chietkhau
    def __lt__(self, other):
        return self.tongtien > other.tongtien
    def __str__(self):
        return f"{self.ma} {self.ten} {self.sl} {self.gia} {self.chietkhau} {self.tongtien}"

a = []
for i in range (int(input())):
    a.append(MatHang(input(), input(), int(input()), int(input()), int(input())))
a.sort()
for x in a:
    print(x)