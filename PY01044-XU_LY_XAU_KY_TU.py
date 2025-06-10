x = set(input().lower().split())
y = set(input().lower().split())
print(" ".join(sorted(x | y)))
print(" ".join(sorted(x & y)))