from collections import Counter

a = []
with open('VANBAN.in', 'r') as file:
    for line in file:
        l = line.split()
        for c in l:
            a.append(c)
b = [x for x in a if x == x[::-1]]
if len(b) > 0:
    c = max(len(x) for x in b)
    k = [x for x in b if len(x) == c]
    cou = Counter(k)
    for key, val in cou.items():
        print(key, val)