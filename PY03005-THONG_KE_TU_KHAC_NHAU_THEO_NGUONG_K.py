import re
from collections import Counter

s = ""
n, k = map(int, input().split())
for i in range (n):
    s += input().lower() + " "
r = re.findall(r'[a-z0-9]+', s)
c = Counter(r)
a = sorted(c.items(), key= lambda x: (-x[1], x[0]))
for key, val in a:
    if val >= k:
        print(key, val)
