from itertools import combinations

n , k = map(int, input().split())
se = {int(x) for x in input().split()}
ss = sorted(se)
for i in combinations(ss, k):
    print(" ".join(map(str,i)))