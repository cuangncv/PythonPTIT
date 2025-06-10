n = input().strip()
while len(n) > 1:
    n = str(int(n[:len(n) // 2]) + int(n[len(n) //2 :]))
    print(n)
