test = int(input())
a = list(map(int, input().split()))[:test]
x = sorted(a)
max1 = x[-1]
max2 = x[-2]
max3 = x[-3]
min1 = x[0]
min2 = x[1]
print(max(max1*max2*max3, max1*max2, min1*min2*max1, min1*min2))