def f(n, k):
    if k == 2**(n-1):
        return n
    if k > 2 ** (n-1):
        return f(n-1,k - 2**(n-1))
    return f(n-1, k)

for i in range (int(input())):
    n, k = map(int, input().split())
    print(chr(f(n, k) + ord('A') - 1))