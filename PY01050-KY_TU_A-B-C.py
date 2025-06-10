def a_b_c (n, cnta, cntb, cntc, s):
    if len(s) >= 3:
        if cnta <= cntb and cntb <= cntc and cnta != 0 :
            k.append(s)
    if len(s) < n:
        a_b_c(n, cnta + 1, cntb, cntc, s + "A")
        a_b_c(n, cnta , cntb + 1, cntc , s + "B")
        a_b_c(n, cnta, cntb, cntc + 1, s + "C")
k = []
a_b_c(int(input()), 0, 0, 0, "")
k.sort(key= lambda x:(len(x), x))
for i in k:
    print(i)