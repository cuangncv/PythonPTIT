from itertools import permutations

for i in range(int(input())):
    n = int(input())
    so = ""
    for x in range(1, n + 1):
        so += str(x)
    a = []
    for s in permutations(so):
        a.append("".join(s))
    a.sort(reverse=True)
    print(len(a))
    print(*a)