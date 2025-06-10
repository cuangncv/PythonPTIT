import pickle
from collections import Counter


def so_khong_giam(n):
    s = str(n)
    if len(s) < 2:
        return False
    for i in range (1, len(n)):
        if int(s[i]) < int(s[i-1]):
            return False
    return True

with open("DATA1.in", 'rb') as f1:
    data1 = pickle.load(f1)
with open("DATA2.in", 'rb') as f2:
    data2 = pickle.load(f2)

cou1 = Counter(data1)
cou2 = Counter(data2)
data = set(data1) & set(data2)
a = [x for x in data if so_khong_giam(x)]
a.sort()
for c in a:
    print(c, cou1[c], cou2[c])

