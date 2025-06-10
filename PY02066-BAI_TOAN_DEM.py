n = int(input())
a = []
while len(a) < n:
    l = list(map(int, input().split()))
    for x in l:
        if len(a) < n:
            a.append(x)
check = False
for i in range (1, max(a)):
    if i not in a:
        print(i)
        check = True
if not check:
    print("Excellent!")