from collections import Counter

for i in range(int(input())):
    n = int(input())
    a = []
    for y in range (n):
        a.append(int(input()))
    cou = Counter(a)
    c = max(cou.values())
    k = [key for key, val in cou.items() if val == c]
    print(min(k))