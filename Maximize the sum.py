for _ in range(int(input())):
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    a_set = set(A)
    a_set = sorted(a_set, reverse=True)
    sum_list = []
    for n in list(a_set)[:K]:
        if n>0:
            sm = int(n)*A.count(int(n))
            sum_list.append(sm)
    print(sum(sum_list))