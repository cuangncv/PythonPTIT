import math

n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range (n - 1):
    for y in range (i+1, n):
        if math.gcd(a[i], a[y]) == 1:
            print(a[i], a[y])