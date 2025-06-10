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
def check (n):
    sum = 0
    for y in range (len(n)):
        sum += int(n[y])
        if y % 2 == 0 and int(n[y]) % 2 != 0:
            return False
        if y % 2 != 0 and int(n[y]) % 2 == 0:
            return False
    if not is_prime(sum):
        return False
    return True
test = int(input().strip())
for i in range (test):
    n = input().strip()
    print("YES" if check(n) else "NO")