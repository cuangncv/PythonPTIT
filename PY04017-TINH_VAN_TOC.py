
class Cuaro:
    def __init__(self, ten, donVi, tg_den_dich):
        self.ten = ten
        self.donVi = donVi
        self.ma =''.join(word[0].upper() for word in self.donVi.split()) + ''.join(word[0].upper() for word in self.ten.split())
        q = tg_den_dich.split(':')
        self.toc_do = 120 / (int(q[0]) - 6 + int(q[1]) /60)

    def __lt__(self, other):
        return self.toc_do > other.toc_do

    def __str__(self):
        return f"{self.ma} {self.ten} {self.donVi} {round(self.toc_do)} Km/h"

cac_cua_ro = []
for i in range(int(input())):
    ten = input()
    donVi = input()
    tgian_vedich = input()
    cac_cua_ro.append(Cuaro(ten, donVi, tgian_vedich))
cac_cua_ro.sort()
for x in cac_cua_ro:
    print(x)

