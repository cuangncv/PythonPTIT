test = int(input().strip())
for i in range (test):
    n = input()
    check = True
    tich = 1
    for i in range(1, len(n), 2):
        if int(n[i]) != 0:
            check = False
            tich *= int(n[i])
    if check:
        tich = 0
    tong = sum(int(n[i]) for i in range(0,len(n),2))
    print(tong, tich)