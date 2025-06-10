n = int(input())
l = list(map(int, input().split()))[:n]
a = []
for i in l:
    a.append(sum(abs(i-x) for x in l))
vlu = min(a)
key = 0
for i in l:
    if sum(abs(i-x) for x in l) == vlu:
        key = i
        break
print(vlu, key)