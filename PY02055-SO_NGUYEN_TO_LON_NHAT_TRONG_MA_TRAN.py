def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
n , m = map(int, input().split())
l = [list(map(int, input().split()))[:m] for i in range(n)]
a = 0
for i in range (n):
    for y in range (m):
        if is_prime(int(l[i][y])) and int(l[i][y]) > a:
            a = int(l[i][y])
if a == 0:
    print("NOT FOUND")
else:
    print(a)
    for i in range(n):
        for y in range(m):
            if int(l[i][y]) == a:
                print(f"Vi tri [{i}][{y}]")