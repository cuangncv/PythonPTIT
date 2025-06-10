test = int(input().strip())
for i in range (test):
    s = input().strip()
    print("YES" if s[0] == s[-1] else "NO")