class ThiSinh:
    def __init__(self, ma, hoTen, d):
        self.ma = ma
        self.hoTen = hoTen
        diem = d[0] + d[1] + sum(d)
        self.trungBinh = round(diem / 12 + 0.01, 1)
    def xep_loai (self):
        if self.trungBinh < 5:
            return "YEU"
        elif self.trungBinh < 7:
            return "TB"
        elif self.trungBinh < 8:
            return "KHA"
        elif self.trungBinh < 9:
            return "GIOI"
        else:
            return "XUAT SAC"
    def __str__(self):
        return f"{self.ma} {self.hoTen} {self.trungBinh} {self.xep_loai()}"

    def __lt__(self, other):
        if self.trungBinh == other.trungBinh:
            return self.ma < other.ma
        return self.trungBinh > other.trungBinh

if __name__ == '__main__':
    ds = []
    for i in range(int(input())):
        hoTen = input().strip()
        d = list(map(float, input().split()))
        ts = ThiSinh("HS{:02d}".format(i + 1), hoTen, d)
        ds.append(ts)
    ds.sort()
    for x in ds:
        print(x)