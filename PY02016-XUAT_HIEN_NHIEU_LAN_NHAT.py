from collections import Counter

for i in range (int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    m = max(c.values())
    k = [key for key, val in c.items() if val == m and val > n /2]
    print(min(k) if k else "NO")