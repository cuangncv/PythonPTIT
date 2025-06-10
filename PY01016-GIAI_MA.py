for i in range (int(input())):
    s = input().strip()
    key = ""
    for y in range (0, len(s), 2):
        key += s[y] * int(s[y+1])
    print(key)