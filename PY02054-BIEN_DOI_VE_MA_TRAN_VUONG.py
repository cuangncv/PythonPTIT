n , m = map(int, input().split())
l = [list(map(int, input().split()))[:m] for i in range(n)]
dem1= 0
if n > m:
    for i in range (n):
        if i % 2 == 1 or dem1 == n-m:
            for y in range (m):
                print(l[i][y], end=" ")
            print()
        else:
            dem1 += 1
else:
    for i in range (n):
        dem2 = 0
        for y in range (m):
            if y % 2 == 0 or dem2 == m - n:
                print(l[i][y], end=" ")
            else:
                dem2 += 1
        print()