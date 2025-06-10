import math

test = int(input().strip())
for i in range (test):
    s = input().strip()
    tong = 0
    for c in s:
        tong += math.factorial(int(c))
    print("Yes" if tong == int(s) else "No" )