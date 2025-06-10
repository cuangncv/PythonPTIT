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
def check(n):
    if not is_prime(int(n)):
        return False
    if not is_prime(int(n[::-1])):
        return False
    s = sum(int(x) for x in n)
    if not is_prime(s):
        return False
    for c in n:
        if not is_prime(int(c)):
            return False
    return True

for i in range (int(input())):
    n = input().strip()
    print("Yes" if check(n) else "No")