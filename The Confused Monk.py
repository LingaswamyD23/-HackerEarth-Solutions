import math
def calc_gcd(x, y):
    while (y):
        x, y = y, x % y
    return x

N = int(input())
arr = list(map(int, input().split()))[:N]
#print(math.gcd(*arr))

if N==1:
    gcdd = arr[0]
else:
    num1 = arr[0]
    num2 = arr[1]
    gcdd = calc_gcd(num1, num2)
    for i in range(2, len(arr)):
        gcdd = calc_gcd(gcdd, arr[i])
print((math.prod(arr)**gcdd)% (10**9 + 7))