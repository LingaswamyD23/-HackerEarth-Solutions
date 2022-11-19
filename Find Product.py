import math
N = int(input())
if 1<=N<=(10**3):
    arr = list(map(int, input().split()))[:N]
    print(math.prod(arr)%(10**9+7))