class HoaDon:
    def __init__(self, i, ten, cscu, csmoi):
        self.ma = f"KH{i+1:02d}"
        self.ten = ten
        self.lgnuoc = csmoi - cscu
    def tinhtien(self):
        if self.lgnuoc <= 50:
            return self.lgnuoc * 102
        # 50m3 đầu tính tiền riêng. tổng phí vẫn là 3%
        elif self.lgnuoc <=100:
            return (self.lgnuoc * 150 - 50 * 50)* 1.03
        else:
            return (self.lgnuoc * 200 - 50 * (100 + 50)) * 1.05
    def __str__(self):
        return f"{self.ma} {self.ten} {round(self.tinhtien())}"
    def __lt__(self, other):
        return self.tinhtien() > other.tinhtien()

a = []
for i in range(int(input())):
    a.append(HoaDon(i, input(), int(input()), int(input())))
a.sort()
for x in a:
    print(x)

