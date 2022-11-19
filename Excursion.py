import math
T = int(input())

for _ in range(T):
    N,M,K = map(int, input().split())
    print(math.ceil(N/K)+math.ceil(M/K))
