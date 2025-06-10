for i in range(int(input())):
    p, q = input().split()
    if p < q:
        p, q = q , p
    s = input().split()
    if (len(s) > 1):
        X1, X2 = s[0], s[1]
    else:
        X1 = s[0]
        X2 = input()

    min_X1 = X1.replace(p, q)
    min_X2 = X2.replace(p, q)

    max_X1 = X1.replace(q, p)
    max_X2 = X2.replace(q, p)

    min_sum = int(min_X1) + int(min_X2)
    max_sum = int(max_X1) + int(max_X2)

    print(min_sum, max_sum)
