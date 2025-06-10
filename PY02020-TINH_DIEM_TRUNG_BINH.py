n = int(input())
a = list(map(float, input().split()))
dem = 0
s = 0
for c in a:
    if c != max(a) and c != min(a):
        s += c
        dem += 1
print(f"{s / dem:.2f}")