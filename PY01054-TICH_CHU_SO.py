import math

for i in range (int(input())):
    n = input()
    print(math.prod(int(x) for x in n if x != '0'))