for _ in range(int(input())):
    N = int(input())
    M = [list(map(int, input().split())) for y in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            for p in range(i,N):
                for q in range(j,N):
                    if M[i][j]>M[p][q]:
                        count +=1
    print(count)