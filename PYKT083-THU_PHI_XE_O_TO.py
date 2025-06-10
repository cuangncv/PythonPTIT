thong_ke = {}

for i in range (int(input())):
    s = input().split()
    if s[4] not in thong_ke:
        thong_ke[s[4]] = 0
    if s[3] == 'IN':
        if s[1] == 'Xe_con':
            if s[2] == '5':
                thong_ke[s[4]] += 10000
            else:
                thong_ke[s[4]] += 15000
        elif s[1] == 'Xe_tai':
            thong_ke[s[4]] += 20000
        else:
            if s[2] == '29':
                thong_ke[s[4]] += 50000
            else:
                thong_ke[s[4]] += 70000
for i in thong_ke:
    print(f"{i}: {thong_ke[i]}")