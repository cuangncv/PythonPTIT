test = int(input().strip())
for x in range (test):
    a = input().strip()
    check = True
    c = 0
    if len(a) < 3:
        check = False
    else:
        for i in range (1, len(a)):
            if a[i] == a[i-1]:
                check = False
                break
            if c == 0:
                if a[i] < a[i-1]:
                   c = 1
            else:
                if a[i] > a[i-1]:
                   check = False
    print("YES" if check else "NO")