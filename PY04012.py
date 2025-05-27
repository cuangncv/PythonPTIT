class SinhVien:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.chuyenCan = 10
        self.ghiChu = ""
    def tinhDiem (self, diemdanh):
        for i in diemdanh:
            if i == 'v':
                self.chuyenCan -= 2
            if i == 'm':
                self.chuyenCan -= 1
        if self.chuyenCan <= 0:
            self.chuyenCan = 0
            self.ghiChu = "KDDK"
    def __str__(self):
        return f"{self.ma} {self.ten} {self.lop} {self.chuyenCan} {self.ghiChu}"

sv = []
test = int(input())
for _ in range (test):
    ma = input().strip()
    ten = input().strip()
    lop = input().strip()
    sv.append(SinhVien(ma, ten, lop))
sv_dict = {sinhvien.ma : sinhvien for sinhvien in sv}
for _ in range (test):
    ma, dd = map(str, input().split())
    sv_dict[ma].tinhDiem(dd)
for x in sv:
    print(x)