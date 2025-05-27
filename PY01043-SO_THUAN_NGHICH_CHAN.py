for i in range (int(input())):
    N = int(input())
    stack = ["8", "6", "4", "2"]
    while True:
        t = stack.pop()
        so = int(t + t[::-1])
        if so < N:
            print(so, end = " ")
        else:
            break
        stack = [t + "8", t + "6", t + "4", t + "2", t + "0"] + stack
    print()