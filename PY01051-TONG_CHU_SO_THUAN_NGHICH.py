for i in range(int(input())):
    tong = str(sum(int(x) for x in input()))
    print("YES" if len(tong) > 1 and tong == tong[::-1] else "NO")