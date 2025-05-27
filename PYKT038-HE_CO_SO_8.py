N = input().strip()
while len(N) % 3 != 0:
    N = "0" + N
key = ""
for i in range(0, len(N), 3):
    x = N[i:i+3]
    s = int(x, 2)
    key += str(s)
print(key)