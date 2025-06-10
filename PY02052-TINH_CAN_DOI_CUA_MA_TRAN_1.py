n = int(input())
a = [list(map(int, input().split())) for x in range(n)]
k = int(input())
tong_tren, tong_duoi = 0, 0
for i in range(n):
    for y in range(n):
        if y > i:
            tong_tren += a[i][y]
        if i > y:
            tong_duoi += a[i][y]
chenh_lech = abs(tong_tren - tong_duoi)
print("YES" if chenh_lech <= k else "NO")
print(chenh_lech)