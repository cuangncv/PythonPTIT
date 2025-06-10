from datetime import datetime


class LuongMua:
    def __init__(self, ten):
        self.ten = ten
        self.lg = 0
        self.tg = 0

    def them (self, batdau, ketthuc, sl):
        t1 = datetime.strptime(batdau, "%H:%M")
        t2 = datetime.strptime(ketthuc, "%H:%M")
        self.tg += (t2-t1).seconds / 3600
        self.lg += sl

    def __str__(self):
        return f"{self.ten} {(self.lg / self.tg):.2f}"


tram = {}
stt = []

for i in range(int(input())):
    ten = input()
    batdau = input()
    ketthuc = input()
    sl = int(input())
    if ten not in tram:
        tram[ten] = LuongMua(ten)
        stt.append(ten)
    tram[ten].them(batdau, ketthuc, sl)
for nm, tr in enumerate(stt, start=1):
    print(f"T{nm:02d} {tram[tr]}")