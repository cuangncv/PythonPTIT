class GiaoVien:
    def __init__(self, ma, ten, mx, diemTin, diemCM):
        self.ma = ma
        self.ten = ten
        self.set_mon(mx)
        self.set_diem(mx, diemTin, diemCM)
        self.set_trangThai()
    def set_mon(self, mx):
        if mx[0] == 'A':
            self.monHoc = 'TOAN'
        elif mx[0] == 'B':
            self.monHoc = 'LY'
        else:
            self.monHoc = 'HOA'
    def set_diem(self, mx, diemTin, diemCM):
        self.tongDiem = diemTin * 2 + diemCM
        if mx[1] == '1':
            self.tongDiem += 2.0
        elif mx[1] == '2':
            self.tongDiem += 1.5
        elif mx[1] == '3':
            self.tongDiem += 1.0
    def set_trangThai(self):
        if self.tongDiem >= 18:
            self.trangThai = 'TRUNG TUYEN'
        else:
            self.trangThai = "LOAI"
    def __str__(self):
        return f"{self.ma} {self.ten} {self.monHoc} {self.tongDiem:.1f} {self.trangThai}"
    def __lt__(self, other):
        return self.tongDiem > other.tongDiem

ds = []
for i in range (int(input())):
    ten = input().strip()
    mx = input().strip()
    diemTin = float(input())
    diemCM = float(input())
    ds.append(GiaoVien("GV{:02d}".format(i+1), ten, mx, diemTin, diemCM))
ds.sort()
for x in ds:
    print(x)