def doi_co_so(n, base):
    if n == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        res = digits[n % base] + res
        n //= base
    return res
for i in range (int(input())):
    n, b = map(int, input().split())
    print(doi_co_so(n, b))
