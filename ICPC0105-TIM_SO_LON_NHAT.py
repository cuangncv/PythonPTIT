import re

for i in range (int(input())):
    x = input().strip()
    r = re.findall(r'\d+', x)
    a = list(map(int, r))
    print(max(a))