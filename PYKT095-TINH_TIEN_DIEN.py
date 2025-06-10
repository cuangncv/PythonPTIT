class TienDien:
    def __init__(self, i, ten, loai, csd, csc):
        self.ma = f"KH{i+1:02d}"
        self.ten = ""
        name = ten.split()
        for c in name:
            self.ten += c.title() + " "
        self.sodien = int(csc) - int(csd)
        if loai == 'A':
            self.dinh_muc = 100
        elif loai == 'B':
            self.dinh_muc = 500
        else:
            self.dinh_muc = 200
    def tien_dinh_muc(self):
        if self.sodien > self.dinh_muc:
            return self.dinh_muc * 450
        return self.sodien * 450
    def tien_vuot(self):
        if self.sodien > self.dinh_muc:
            return (self.sodien - self.dinh_muc) * 1000
        return 0
    def vat(self):
        return self.tien_vuot() // 20
    def tongtien(self):
        return self.tien_vuot() + self.tien_dinh_muc() + self.vat()
    def __str__(self):
        return f"{self.ma} {self.ten}{self.tien_dinh_muc()} {self.tien_vuot()} {self.vat()} {self.tongtien()}"
    def __lt__(self, other):
        return self.tongtien() > other.tongtien()

ds = []
for i in range (int(input())):
    ten = input().strip()
    loai, csd, csc = input().split()
    ds.append(TienDien(i, ten, loai, csd, csc))
ds.sort()
for x in ds:
    print(x)