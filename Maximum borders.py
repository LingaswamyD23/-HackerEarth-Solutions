T = int(input())
for _ in range(T):
    br = []
    n, m = map(int, input().split())

    out = [list(input()) for i in range(n)]
    for i in range(n):
        br.append(out[i].count('#'))
    
    print(max(br))
    