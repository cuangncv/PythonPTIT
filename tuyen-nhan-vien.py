class ThiSinh:
    def __init__(self, ma, hoTen, d1, d2):
        self.ma = ma
        self.hoTen = hoTen
        self.trungBinh = (d1 + d2) / 2
    def xep_loai (self):
        if self.trungBinh < 5:
            return "TRUOT"
        elif self.trungBinh < 8:
            return "CAN NHAC"
        elif self.trungBinh <= 9.5:
            return "DAT"
        else:
            return "XUAT SAC"
    def __str__(self):
        return f"{self.ma} {self.hoTen} {self.trungBinh:.2f} {self.xep_loai()}"

    def __lt__(self, other):
        return self.trungBinh > other.trungBinh

if __name__ == '__main__':
    ds = []
    for i in range(int(input())):
        hoTen = input().strip()
        d1 = float(input())
        d2 = float(input())
        if d1 > 10:
            d1 /= 10
        if d2 > 10:
            d2 /= 10
        ts = ThiSinh("TS0" + str(i+1), hoTen, d1, d2)
        ds.append(ts)
    ds.sort()
    for x in ds:
        print(x)