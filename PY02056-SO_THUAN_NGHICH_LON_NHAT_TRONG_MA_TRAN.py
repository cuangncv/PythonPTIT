n , m = map(int, input().split())
l = [list(map(int, input().split()))[:m] for i in range(n)]
a = 0
for i in range (n):
    for y in range (m):
        q = str(l[i][y])
        if q == q[::-1] and len(q) > 1 and l[i][y] > a:
            a = l[i][y]
if a == 0:
    print("NOT FOUND")
else:
    print(a)
    for i in range(n):
        for y in range(m):
            if l[i][y] == a:
                print(f"Vi tri [{i}][{y}]")