T = int(input())
if 1<=T <=20:
    for _ in range(T):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        x = K%N
        print(*(arr[N-x:]+arr[:N-x]))