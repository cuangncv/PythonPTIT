a = []
while len(a) < 10:
    s = list(map(int, input().split()))
    for c in s:
        if len(a) == 10:
            break
        a.append(c)
se = {int(x % 42) for x in a}
print(len(se))