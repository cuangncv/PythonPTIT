from itertools import permutations

s = input().strip()
p = permutations(s)
for i in p:
    print("".join(i))