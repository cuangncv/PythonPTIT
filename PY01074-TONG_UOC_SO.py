import math

def snt_arr(x):
    a = [True] * x
    a[0] = a[1] = False
    snt = []
    for i in range (2, x):
        if a[i] == True:
            snt.append(i)
            for y in range (i*i, x, i):
                a[y] = False
    return snt

tong = 0
for i in range(int(input())):
    x = int(input())
    snt = snt_arr(int(math.isqrt(x)) + 1)
    for y in snt:
        while x % y == 0:
            tong += y
            x //= y
    if x > 1:
        tong += x
print(tong)