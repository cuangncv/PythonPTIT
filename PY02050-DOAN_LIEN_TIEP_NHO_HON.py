for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    stack = []
    result = [0]*n

    for i in range(n):
        start = i
        while stack and stack[-1][0] <= arr[i]:
            start = stack[-1][1]
            stack.pop()
        stack.append((arr[i], start))
        result[i] = i - start + 1

    print(*result)
