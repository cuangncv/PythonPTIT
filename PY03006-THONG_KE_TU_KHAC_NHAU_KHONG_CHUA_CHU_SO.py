import re
from collections import Counter

n = int(input())
line = ""
for i in range (n):
    line += input().lower() + " "
r = re.findall(r'[a-z]+', line)
se = Counter(r)
a = sorted(se.items(), key= lambda x: (-x[1], x[0]))
for key, val in a:
    print(key, val)
