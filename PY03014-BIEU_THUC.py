for i in range (int(input())):
    s = input()
    pointer = 0
    stack = []
    for c in s:
        if c == '(':
            pointer += 1
            stack.append(pointer)
            print(pointer, end= " ")
        elif c == ')':
            print(stack.pop(), end= " ")
    print()