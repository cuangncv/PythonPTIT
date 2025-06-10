class DanhBa:
    def __init__(self, hoten, sdt, ngay):
        h = hoten.split()
        self.ten = h[-1]
        self.hodem = " ".join(h[:-1])
        self.sdt = sdt
        self.ngay = ngay
    def __lt__(self, other):
        if self.ten == other.ten:
            return self.hodem < other.hodem
        return self.ten < other.ten
    def __str__(self):
        return f"{self.hodem} {self.ten}: {self.sdt} {self.ngay}"

db = []
ngay = ""
nd = []
with open('SOTAY.txt', 'r') as file:
    for line in file:
        nd.append(line.strip())
i = 0
while i < len(nd):
    if nd[i].startswith("Ngay "):
        ngay = nd[i][5:]
        i += 1
    else:
        db.append(DanhBa(nd[i], nd[i+1], ngay))
        i += 2
db.sort()
with open('DIENTHOAI.txt', 'w') as f:
    for x in db:
        f.write(f'{x}\n')