from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
counter  = Counter (a)
b = set(counter.values())
lt = sorted(b, reverse= True)
if len(lt) == 1:
    print("NONE")
else:
    x = lt[1]
    for i in a:
        if counter[i] == x:
            print(i)
            break