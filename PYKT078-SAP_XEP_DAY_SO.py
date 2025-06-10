for i in range (int(input())):
    n , m = map(int, input().split())
    l = list(map(int, input().split()))[:n]
    maxv = max(l)
    for y in range(len(l)):
        if l[y] == maxv:
            l.insert(y, m)
            break
    a = [x for x in l if x < 0]
    b = [x for x in l if x >= 0]
    key = a + b
    print(*key)