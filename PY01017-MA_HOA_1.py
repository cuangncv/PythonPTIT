for i in range (int(input())):
    s = input().strip()
    dem = 1
    key = ""
    for y in range(len(s) - 1):
        if s[y] == s[y+1]:
            dem += 1
        else:
            print(str(dem) + s[y], end="")
            dem = 1
    print(str(dem) + s[-1])