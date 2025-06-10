for i in range(int(input())):
    ip = input().strip()
    a = ip.split(".")
    check = True
    if len(a) != 4:
        check = False
    for x in a:
        if not x.isdigit():
            check = False
        elif not 0 <= int(x) <= 255:
            check = False
    print("YES" if check else "NO")