def snt(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

n = int(input())
a = list(map(int, input().split()))
l = list(dict.fromkeys(a))
t = sum(l)
s = 0
check = False
for i in range (len(l)):
    s += l[i]
    if snt(s) and snt(t-s):
        print(i)
        check = True
        break
if not check:
    print("NOT FOUND")