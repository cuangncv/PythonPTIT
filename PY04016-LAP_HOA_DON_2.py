from datetime import datetime


class KhachHang:
    def __init__(self, i, ten, sophong, ngaynhan, ngaytra, phatsinh):
        self.ma = f"KH{i+1:02d}"
        self.ten = ten
        self.soPhong = sophong
        ngayNhan = datetime.strptime(ngaynhan, '%d/%m/%Y')
        ngayTra = datetime.strptime(ngaytra, '%d/%m/%Y')
        self.soNgay = (ngayTra - ngayNhan).days + 1
        self.phatsinh = phatsinh
    def tinhTien (self):
        gia = 0
        if self.soPhong[0] == "1":
            gia = 25
        elif self.soPhong[0] == "2":
            gia = 34
        elif self.soPhong[0] == "3":
            gia = 50
        else:
            gia = 80
        return self.soNgay * gia + self.phatsinh
    def __lt__(self, other):
        return self.tinhTien() > other.tinhTien()
    def __str__(self):
        return f"{self.ma} {self.ten} {self.soPhong} {self.soNgay} {self.tinhTien()}"

a = []
for i in range (int(input())):
    a.append(KhachHang(i, input().strip(), input().strip(), input().strip(), input().strip(), int(input())))
a.sort()
for x in a:
    print(x)
