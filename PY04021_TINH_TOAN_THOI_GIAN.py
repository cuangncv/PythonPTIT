from datetime import datetime


class GameThu:
    def __init__(self, ma, ten, giovao, giora):
        self.ma = ma
        self.ten = ten
        tgv = datetime.strptime(giovao, "%H:%M")
        tgr = datetime.strptime(giora, "%H:%M")
        self.tgs = tgr - tgv
        self.soGio = self.tgs.seconds // 3600
        self.soPhut = (self.tgs.seconds % 3600) // 60
    def __str__(self):
        return f"{self.ma} {self.ten} {self.soGio} gio {self.soPhut} phut"
    def __lt__(self, other):
        return self.tgs > other.tgs

a = []
for i in range(int(input())):
    a.append(GameThu(input(), input(), input(), input()))
a.sort()
for x in a:
    print(x)