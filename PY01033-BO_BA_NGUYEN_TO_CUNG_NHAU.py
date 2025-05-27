import math

def solve(i, arr, cnt):
    if cnt == 3:
        a, b, c = arr
        if math.gcd(a, b) == 1 and math.gcd(b, c) == 1 and math.gcd(a, c) == 1:
            print("({}, {}, {})".format(a, b, c))
        return
    for j in range(i+1, r+1):
        solve(j, arr + [j], cnt+1)


global r
l, r = map(int, input().split())
for i in range(l, r+1):
    solve(i, [i], 1)