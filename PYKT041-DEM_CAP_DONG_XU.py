def demcap(n, l):
    demcot = [0] * n
    demhang = [0] * n
    for i in range (n):
        for y in range (n):
            if l[i][y] == 'C':
                demcot[y] += 1
                demhang[i] += 1
    caphang = sum(c * (c - 1) // 2 for c in demhang)
    capcot = sum(c * (c - 1) // 2 for c in demcot)
    return caphang + capcot
n = int(input())
l = [input().strip() for i in range(n)]
print(demcap(n,l))