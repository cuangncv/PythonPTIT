sl = 0
check = False
stt = 0
ds = []
for i in range (int(input())):
    a = input().split()
    if (len(a) == 6 or len(a) == 8) and not check:
        sl += 1
        ds.append("1")
        check = True
    if len(a) == 7:
        check = False
        stt += 1
    if stt == 4:
        sl += 1
        ds.append("2")
        stt = 0
print(sl)
for x in ds:
    print(x)