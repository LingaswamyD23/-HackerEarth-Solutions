MOD = int(10**9+7)

for _ in range(int(input())):
    minx = maxx = 0
    n = int(input())
    maxx = (n*(n-1)*(2*n-1)//6)%MOD
    #ans = n*(n - 1)*(2n - 1)/6
    no_of_matches = n - 1 #all players except you
    wins = no_of_matches//2 #Everyone wins half their match
    minx = (n*wins*wins)%MOD
    print(minx, maxx)
