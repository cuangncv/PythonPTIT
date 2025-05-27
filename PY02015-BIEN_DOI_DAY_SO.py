while True:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0:
        break
    dem = 0
    while not a == b == c ==d :
        ai = a
        bi = b
        ci = c
        di = d
        a = abs(ai - bi)
        b = abs(bi - ci)
        c = abs(ci - di)
        d = abs(di - ai)
        dem += 1
    print(dem)
