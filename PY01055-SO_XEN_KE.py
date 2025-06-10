test = int(input().strip())
for i in range (test):
    n = input().strip()
    check = True
    if len(n) % 2 == 0 or n[0] == n[1]:
        check = False
    for y in range (2,len(n),2):
        if n[y] != n[0]:
            check = False
    print("YES" if check else "NO")