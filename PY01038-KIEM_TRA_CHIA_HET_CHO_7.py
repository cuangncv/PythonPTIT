for i in range(int(input())):
    n = input()
    if int(n) % 7 == 0:
        print(n)
    else:
        check = False
        for y in range ( 1000 ):
            z = n[::-1]
            if (int(n) + int(z)) % 7 == 0:
                check = True
                print(int(n) + int(z))
                break
            else:
                n = str(int(n) + int(z))
        if not check:
            print("-1")