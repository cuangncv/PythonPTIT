import re

s = ""
for i in range (int(input())):
    s += input() + " "
r = re.findall(r'[0-9]+', s)
a = [int(x) for x in r]
a.sort()
for c in a:
    print(c)