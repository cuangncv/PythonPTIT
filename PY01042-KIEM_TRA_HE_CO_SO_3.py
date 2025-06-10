for i in range (int(input())):
    print("YES" if all(x in'012' for x in input()) else "NO")