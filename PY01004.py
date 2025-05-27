import math


def euler(n):
    key = n
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            key -= key // i
        i += 1
    if n > 1:
        key -= key // n
    return key
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

t = int(input().strip())
for x in range(t):
    n = int(input().strip())
    k = euler(n)
    if is_prime(k):
        print("YES")
    else:
        print("NO")