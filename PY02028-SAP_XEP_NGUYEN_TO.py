def snt(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

n = int(input())
a = list(map(int, input().split()))
b = [x for x in a if snt(x)]
b = iter(sorted(b))
for c in a:
    if snt(c):
        print(next(b), end=" ")
    else:
        print(c, end=" ")