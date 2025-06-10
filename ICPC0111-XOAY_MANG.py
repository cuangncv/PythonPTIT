test = int(input().strip())
for i in range (test):
    N , d = map(int, input().split())
    n = list(map(int, input().split()))[:N]
    print(*n[d:], *n[:d])