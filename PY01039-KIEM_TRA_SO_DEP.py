test = int(input().strip())
for x in range (test):
    a = input().strip()
    check = True
    if a[0] == a[1]:
        check = False
    for i in range (2,len(a)):
        if i % 2 == 0:
            if a[i] != a[0]:
                check = False
                break
        else:
            if a[i] != a[1]:
                check = False
                break
    print("YES" if check else "NO")