class SinhVien:
    def __init__(self, hoTen, soBaiDung, luotSubmit):
        self.hoTen = hoTen
        self.soBaiDung = soBaiDung
        self.luotSubmit = luotSubmit
    def __str__(self):
        return f"{self.hoTen} {self.soBaiDung} {self.luotSubmit}"
    def __lt__(self, other):
        if self.soBaiDung == other.soBaiDung:
            if self.luotSubmit == other.luotSubmit:
                return self.hoTen < other.hoTen
            return self.luotSubmit < other.luotSubmit
        return self.soBaiDung > other.soBaiDung

ds = []
for i in range (int(input())):
    ten = input().strip()
    a, b = map(int, input().split())
    ds.append(SinhVien(ten, a, b))
ds.sort()
for x in ds:
    print(x)