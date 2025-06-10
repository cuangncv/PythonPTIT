for i in range (int(input())):
    n, x, m = map(float, input().split())
    year = 0
    while n < m:
        n += n * x / 100
        year += 1
    print(year)