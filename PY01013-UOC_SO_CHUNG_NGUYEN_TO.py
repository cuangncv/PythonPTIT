import math


def is_ngto(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 ==0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for i in range (int(input())):
    a, b = map(int, input().split())
    uc = math.gcd(a, b)
    print ("YES" if is_ngto(sum(int(x) for x in str(uc))) else "NO")