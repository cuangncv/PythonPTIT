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
n = int(input())
a = list(map(int, input().split()))[:n]
d = list(dict.fromkeys(a))
for i in d:
    if is_prime(i):
        print(i, a.count(i))