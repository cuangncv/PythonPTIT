for i in range (int(input())):
    n = int(input().strip())
    s = 10
    while n >= s:
        x = n % s
        n -= x
        if x >= s // 2:
            n += s
        s *= 10
    print(n)