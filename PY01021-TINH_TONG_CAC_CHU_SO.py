import re

test = int(input())
for i in range (test):
    s = input().strip()
    so = re.findall(r'\d',s)
    chu = re.findall(r'\D',s)
    print("".join(sorted(chu)) + str(sum(map(int, so))))