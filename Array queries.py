def cal_F(N, M, A, B):
    F = 0
    for i in range(N):
        for j in range(M):
            F +=A[i]*B[j]*((i+1)+(j+1))
    return F

def array_queries (N, M, A, B, Q, queries):
    f_sum_list = []
    f_sum_list.append(cal_F(N, M, A, B))
    for q in range(Q):
        if queries[q][0] == 1:
            A[queries[q][1]-1], B[queries[q][2]-1] = B[queries[q][2]-1], A[queries[q][1]-1]
            f_sum_list.append(cal_F(N, M, A, B))
        elif queries[q][0] == 2:
            A[queries[q][1]-1], A[queries[q][2]-1] = A[queries[q][2]-1], A[queries[q][1]-1]
            f_sum_list.append(cal_F(N, M, A, B))
        elif queries[q][0] == 3:
            B[queries[q][1]-1], B[queries[q][2]-1] = B[queries[q][2]-1], B[queries[q][1]-1]
            f_sum_list.append(cal_F(N, M, A, B))
    return f_sum_list


T = int(input())
for _ in range(T):
    N = int(input())
    M = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for i in range(Q)]

    out_ = array_queries(N, M, A, B, Q, queries)
    print (' '.join(map(str, out_)))