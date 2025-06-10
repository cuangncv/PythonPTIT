def tong(x):
    return sum(int(z) for z in x)
for i in range (int(input())):
    n = int(input())
    a = list(map(str, input().split()))[:n]
    a.sort(key= lambda x:(tong(x), int(x)))
    print(*a)