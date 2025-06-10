from collections import Counter

n = input().strip()
k = int(input())
a = []
for i in range (1, len(n), 2):
    a.append(n[i-1] + n[i])
a.sort()
coun = Counter(a)
check = False
for key, val in coun.items():
    if val >= k:
        print(key, val)
        check = True
if not check:
    print("NOT FOUND")