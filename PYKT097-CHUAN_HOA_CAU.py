a = []
while True:
    try:
        s = input().strip().capitalize()
        if s[-1] not in '.!?':
            s += '.'
        k = ""
        q = s.split()
        for i in range(len(q) - 2):
            k += q + " "
        if q[-1] not in '.!?':
            k += q[-2] + " " + q[-1]
        else:
            k += q[-2] + q[-1]
        a.append(k)
    except EOFError:
        break
for c in a:
    print(c)