def check (n, k, u, v, a):
    if k == u or k == v:
        return False
    visit = [False] * (n+1)
    stack = [u]
    visit[u] = True

    while stack:
        x = stack.pop()
        if x == v:
            return False
        for z in a[x]:
            if not visit[z] and z != k:
                stack.append(z)
                visit[z] = True
    return True
def dem_so_dinh(n, m, u, v, ck):
    a = [[] for q in range(n+1)]
    for x, y in ck:
        a[x].append(y)
    return sum(check(n, k, u, v, a) for k in range (1, n+1))
for i in range (int(input())):
    N, M , u , v = map(int, input().split())
    ck = [tuple(map(int, input().split())) for c in range (M)]
    print(dem_so_dinh(N, M ,u, v, ck))


