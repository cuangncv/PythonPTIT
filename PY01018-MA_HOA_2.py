P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    test = input().split()
    if test[0] == "0":
        break
    key = ""
    for x in test[1]:
        key += P[(P.index(x) + int(test[0])) % 28]
    print(key[::-1])