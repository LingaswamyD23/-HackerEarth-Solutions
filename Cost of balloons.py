T = int(input())
if 1<=T<=10:
    for _ in range(T):
        gbc, pbc = map(int, input().split())
        n = int(input())
        g_sum = 0
        p_sum = 0
        if 1<=n<=10:
            for _ in range(n):
                i, j = map(int, input().split())
                g_sum +=i
                p_sum +=j
            gp_cost = g_sum*gbc + p_sum*pbc
            pg_cost = g_sum*pbc + p_sum*gbc
            print(min((g_sum*gbc + p_sum*pbc), (g_sum*pbc + p_sum*gbc)))