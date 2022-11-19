T = int(input())
for _ in range(T):
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))[:M]
    arr.sort()
    count = 0
    i = 0
    while N>0 and i<M:
        if arr[i]<=N:
            count +=1
            N -=arr[i]
        i +=1
    print(count)
