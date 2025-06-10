n = input().strip()
a = []
for i in range (1, len(n), 2):
    a.append(n[i-1] + n[i])
A = list(dict.fromkeys(a))
for c in A:
    print(c, a.count(c))