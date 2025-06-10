def check(n):
    if sum(int(x) for x in n) % 10 != 0:
        return False
    for i in range (len(n) - 1):
        if abs(int(n[i]) - int(n[i+1])) != 2:
            return False
    return True

for i in range(int(input())):
    n = input().strip()
    print("YES" if check(n) else "NO")