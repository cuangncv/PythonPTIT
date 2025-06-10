n = input()
a = []
for i in range (1, len(n), 2):
    a.append(n[i-1] + n[i])
l = list(dict.fromkeys(a))
print(*l)