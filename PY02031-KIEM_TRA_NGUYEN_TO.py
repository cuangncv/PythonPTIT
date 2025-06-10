def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i+2) == 0:
            return False
        i += 6
    return True
n, m = map(int, input().split())
a = [list(map(int, input().split())) for x in range(n)]
for i in range (n):
    for y in range (m):
        if is_prime(a[i][y]):
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()