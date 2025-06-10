class ThiS:
    def __init__(self, ma, ten, team):
        self.ma = ma
        self.ten = ten
        self.team = ds[int(team[-2:]) - 1]
    def __lt__(self, other):
        return self.ten < other.ten
    def __str__(self):
        return f"{self.ma} {self.ten} {self.team}"


ds = []
ts = []
for i in range (int(input())):
    team = input().strip()
    school = input().strip()
    ds.append(team + " " + school)
for i in range (int(input())):
    ts.append(ThiS(f"C{i+1:03d}", input().strip(), input().strip()))
ts.sort()
for x in ts:
    print(x)

