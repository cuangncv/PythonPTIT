test = int(input())
a = []
c = []
l = []
while len(a) < test:
    x = list(map(int, input().split()))
    for i in x:
        if len(a) < test:
            a.append(i)
            if i % 2 == 0:
                c.append(i)
            else:
                l.append(i)
cx = iter(sorted(c))
lx = iter(sorted(l, reverse= True))
for i in a:
    if i % 2 == 0:
        print(next(cx), end=" ")
    else:
        print(next(lx), end=" ")