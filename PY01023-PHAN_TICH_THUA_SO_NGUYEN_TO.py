import math

for i in range (int(input())):
    N = int(input())
    key ="1"
    for y in range(2, int(math.sqrt(N)) + 1):
        if N % y == 0:
            dem = 0
            while N % y == 0:
                dem += 1
                N /= y
            key += f" * {y}^{dem}"
    if N > 1:
        key += f" * {int(N)}^1"
    print(key)