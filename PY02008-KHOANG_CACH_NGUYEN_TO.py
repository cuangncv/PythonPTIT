def snt(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

a = []
for q in range (100001):
    if snt(q):
        a.append(q)
n, x = map(int, input().split())
print(x, end=" ")
for i in range (0, n):
    print(x + a[i], end=" ")
    x += a[i]