test = int(input())
for i in range (test):
    n = int(input())
    a = list(map(int, input().split()))[:n]
    se = set(a)
    print(max(se)-min(se)-len(se)+1)