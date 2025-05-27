n, q = map(int, input().split())
dem = [0] * (n + 2)

for _ in range(q):
    trai, phai = map(int, input().split())
    dem[trai] += 1
    dem[phai + 1] -= 1

for i in range(1, n + 1):
    dem[i] += dem[i - 1]

for i in range(1, n + 1):
    print(dem[i] % 2, end=' ')
