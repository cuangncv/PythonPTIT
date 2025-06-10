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
test = int(input())
for i in range (test):
    s = input()
    check = True
    for y in range (len(s)):
        if s[y] in '2357' and not is_prime(y):
            check = False
        if s[y] not in '2357' and is_prime(y):
            check = False
    print("YES" if check else "NO")