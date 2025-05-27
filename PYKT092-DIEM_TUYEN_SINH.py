class ThiSinh:
    def __init__(self, i, ten, diem, dantoc, khuvuc):
        self.ma = f"TS{i+1:02d}"
        self.ten = self.chuanHoaTen(ten)
        self.diem = self.diemTong(diem, dantoc, khuvuc)
        self.trangThai = self.trangThai(self.diem)

    def chuanHoaTen (self, ten):
        words = map(str, ten.strip().split())
        hoten = ""
        for x in words:
            hoten += x[0].upper()+x[1:].lower()+" "
        return hoten
    def diemTong(self, diem, dantoc, khuvuc):
        tongdiem = diem
        if dantoc != 'Kinh':
            tongdiem += 1.5
        if khuvuc == 1:
            tongdiem += 1.5
        elif khuvuc == 2:
            tongdiem += 1
        return tongdiem
    def trangThai(self, d):
        if d >= 20.5:
            return "Do"
        else:
            return "Truot"
    def __lt__(self, other):
        if self.diem == other.diem:
            return self.ma < other.ma
        return self.diem > other.diem
    def __str__(self):
        return f"{self.ma} {self.ten}{self.diem:.1f} {self.trangThai}"

a = []
for i in range (int(input())):
    a.append(ThiSinh(i, input(), float(input()), input(), int(input())))
a.sort()
for x in a:
    print(x)
